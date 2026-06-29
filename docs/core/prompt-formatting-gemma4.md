# Gemma 4 Prompt Formatting

Starting with Gemma 4, we introduce new control tokens. For Gemma 3 and lower,
see the [previous document](/core/prompt-structure).

The following sections specify the control tokens used by Gemma 4 and their use
cases. Note that the control tokens are reserved in and specific to our
tokenizer.

* Token to indicate a system instruction: `system`
* Token to indicate a user turn: `user`
* Token to indicate a model turn: `model`
* Token to indicate the beginning of a dialogue turn: `<|turn>`
* Token to indicate the end of a dialogue turn: `<turn|>`

Here's an example dialogue:

```text
<|turn>system
You are a helpful assistant.<turn|>
<|turn>user
Hello.<turn|>
```

## Multi-modalities

| Multimodal Token | Purpose |
| :--- | :--- |
| `<\|image>` <br> `<image\|>` | Indicate image embeddings |
| `<\|audio>` <br> `<audio\|>` | Indicate audio embeddings |
| `<\|image\|>` <br> `<\|audio\|>` | Special placeholder tokens |

We use two special placeholder tokens (`<|image|>` and `<|audio|>`) to specify
where image and audio tokens should be inserted. After tokenization, these
tokens are replaced by the actual soft embeddings inside the model.

Here is an example dialogue:

```Python
prompt = """<|turn>user
Describe this image: <|image|>

And translate these audio:

a. <|audio|>
b. <|audio|><turn|>
<|turn>model"""
```

### Audio

For the optimal results, use the following prompt structures. You can also
use a basic `transcribe the audio` prompt.

*   **Audio Speech Recognition (ASR)**

```text
Transcribe the following speech segment in {LANGUAGE} into {LANGUAGE} text.

Follow these specific instructions for formatting the answer:
*   Only output the transcription, with no newlines.
*   When transcribing numbers, write the digits, i.e. write 1.7 and not one point seven, and write 3 instead of three.
```

*   **Automatic Speech Translation (AST)**

```text
Transcribe the following speech segment in {SOURCE_LANGUAGE}, then translate it into {TARGET_LANGUAGE}.
When formatting the answer, first output the transcription in {SOURCE_LANGUAGE}, then one newline, then output the string '{TARGET_LANGUAGE}: ', then the translation in {TARGET_LANGUAGE}.
```

But just `transcribe the audio` should work too.

## Agentic and Reasoning Control Tokens

To support agentic workflows, Gemma uses specialized control tokens that
delineate internal reasoning (thinking) from external actions (function
calling). These tokens allow the model to process complex logic before providing
a final response or interacting with outside tools.

### Function Calling

Gemma 4 is trained on six special tokens to manage the "tool use" lifecycle.

| Token Pair | Purpose |
| :--- | :--- |
| `<\|tool>` <br> `<tool\|>` | Defines a tool |
| `<\|tool_call>` <br> `<tool_call\|>` | Indicates a model's request to use a tool. |
| `<\|tool_response>` <br> `<tool_response\|>` | Provides a tool's execution result back to the model. |

Note: `<|tool_response>` acts as an additional stop sequence for the inference
engine.

**Delimiter for String Values: `<|"|>`**

A single token, `<|"|>`, is used as a delimiter for **all string values**
within the structured data blocks.

*   **Purpose:** This token ensures that any special characters (such as `{`,
    `}`, `,`, or quotes) inside a string are treated as literal text and not as
    part of the data structure's underlying syntax.
*   **Usage:** All string literals in your function declarations, calls, and
    responses must be enclosed using this token (e.g., `key:<|"|>string
    value<|"|>`).

{# disableFinding(HEADING_GERUND) #}
### Thinking Mode

To activate thinking mode, include the `<|think|>` control token within the
system instruction.

| Control Token | Purpose |
| :--- | :--- |
| `<\|think\|>` | Activates thinking mode |
| `<\|channel>` <br> `<channel\|>` | Indicates a model's internal process. |

Note: `<|channel>` is always followed by the word "thought" when thinking mode
is active.

Here is an example dialogue:

```text
<|turn>system
<|think|><turn|>
<|turn>user
What is the water formula?<turn|>
<|turn>model
<|channel>thought
...
<channel|>The most common interpretation of "the water formula" refers...<turn|>
```

Thinking mode is designed to be enabled at the conversation level. This should
be consolidated into a single system turn alongside your other system
instructions, such as tool definitions.

{# disableFinding(HEADING_GERUND) #}
### Reasoning and Function Calling Example

In an agentic turn, the model may "think" privately before deciding to call a
function. The lifecycle follows this sequence:

1. User Inquiry: The user asks a question.
2. Internal Reasoning: The model thinks privately in the thought channel.
3. Tool Request: The model halts generation to request a tool call.
4. Execution & Injection: The application executes the tool and appends the response.
5. Final Response: The model reads the response and generates the final answer.

The following example demonstrates a model using a weather tool:

```text
<|turn>system
<|think|>You are a helpful assistant.<|tool>declaration:get_current_temperature{...}<tool|><turn|>
<|turn>user
What's the temperature in London?<turn|>
<|turn>model
<|channel>thought
...
<channel|><|tool_call>call:get_current_temperature{location:<|"|>London<|"|>}<tool_call|><|tool_response>
```

Your application should parse the model's response to extract the function name
and arguments, execute the function, and then append the `tool_calls` and
`tool_responses` to the chat history under the `assistant` role.

```text
<|turn>model
<|tool_call>call:get_current_weather{location:<|"|>London<|"|>}<tool_call|><|tool_response>response:get_current_weather{temperature:15,weather:<|"|>sunny<|"|>}<tool_response|>
```

Finally, Gemma reads the tool response and replies to the user.

```text
The temperature in London is 15 degrees and it is sunny.<turn|>
```

Here is the complete JSON chat history for this example:

```json
[
  {
    "role": "system",
    "content": "You are a helpful assistant."
  },
  {
    "role": "user",
    "content": "What's the temperature in London?"
  },
  {
    "role": "assistant",
    "tool_calls": [
      {
        "function": {
          "name": "get_current_weather",
          "arguments": {
            "location": "London"
          }
        }
      }
    ],
    "tool_responses": [
      {
        "name": "get_current_weather",
        "response": {
          "temperature": 15,
          "weather": "sunny"
        }
      }
    ],
    "content": "The temperature in London is 15 degrees and it is sunny."
  }
]
```

### Managing Thought Context Between Turns

Properly managing the model's generated thoughts is critical for maintaining
performance across multi-turn conversations.

*   **Standard Multi-Turn Conversations:** You must remove (strip) the model's
    generated thoughts from the previous turn before passing the conversation
    history back to the model for the next turn. If you want to disable thinking
    mode mid-conversation, you can remove the `<|think|>` token when you strip
    the previous thoughts.
*   **Function Calling (Exception):** If a single model turn involves function
    or tool calls, thoughts must **NOT** be removed between the function calls.

**Agentic Workflows and Long-Running Tasks**

Because raw thoughts are stripped between standard turns, developers building
long-running agents may want to retain reasoning context to prevent the model
from entering cyclical reasoning loops.

*   **Summarizing Thoughts:** A highly recommended inference technique is to
    extract, summarize, and feed the model's previous thoughts back into the
    context window as standard text.
*   **Formatting Constraints:** Because Gemma 4 was not explicitly trained with
    raw thoughts included in the prompt (outside of the specific tool-call
    scenario mentioned above), there is no strict or specific format expected by
    the model for these injected thoughts. You have the flexibility to format
    summarized reasoning in whatever way best suits your specific agentic
    architecture.

## Integration Notes

*   **Internal State:** The `<|channel>` and `<channel|>` tokens are typically
    used for Chain-of-Thought (CoT) processing. In standard user-facing
    applications, this content is usually hidden from the end-user.
*   **Tool Loop:** The `tool_call` and `tool_response` tokens facilitate a
    "handshake" between the model your application environment. The application
    intercepts the `tool_call`, executes the underlying code, and feeds the
    result back to the model within the `tool_response` tokens.
*   **Model Behavior:** Larger models (e.g., gemma-4-26B-A4B-it, gemma-4-31B-it)
    may occasionally generate a thought channel even when thinking mode is
    explicitly turned off. To stabilize model behavior in these edge cases,
    consider adding an empty thinking token to the prompt.

## Tip: Fine-Tuning Big Models with No-Thinking Datasets

When fine-tuning gemma-4-26B-A4B-it and gemma-4-31B-it with a dataset that does
not include thinking, you can achieve better results by adding the empty channel
to your training prompts:

```text
<|turn>model
<|channel>thought
<channel|>
```

## Tip: Adaptive Thought Efficiency using System Instructions

While "thinking" in Gemma 4 is officially supported as an ON or OFF boolean
feature, the model has exceptionally strong instruction-following capabilities
that allow you to modulate its thinking behavior dynamically.

Rather than relying on a hardcoded framework parameter for "high" or "low"
thinking, you can use System Instructions (SI) to guide the model into a reduced
thinking mode. By explicitly instructing the model to think efficiently or at a
lower depth (a concept we refer to as a "LOW" thinking instruction), you can
achieve adaptive thought efficiency.

*   **Reduced Cost:** Testing has shown that applying a "LOW" thinking System
    Instruction can reduce the number of thinking tokens generated by
    approximately 20%.
*   **Proof of Concept:** Because this behavior is a byproduct of the model's
    instructability rather than a specifically trained, there is no single
    "perfect" prompt. The "LOW" instruction is a proof of concept.
*   **Customization:** We highly encourage developers to play around with their
    own custom System Instructions. You can fine-tune the depth, length, and
    style of the model's thinking process to perfectly balance latency, cost,
    and output quality for your specific use cases.