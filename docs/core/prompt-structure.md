# Gemma formatting and system instructions

Gemma instruction-tuned (IT) models are trained with a specific *formatter* that
annotates all instruction tuning examples with extra information, both at
training and inference time. The formatter has two purposes:

1.  Indicating roles in a conversation, such as the *system*, *user*, or
   *assistant* roles.
2.  Delineating turns in a conversation, especially in a multi-turn
    conversation.

Below, we specify the control tokens used by Gemma and their use cases. Note
that the control tokens are reserved in and specific to our tokenizer.

*   Token to indicate a user turn: `user`
*   Token to indicate a model turn: `model`
*   Token to indicate the beginning of dialogue turn: `<start_of_turn>`
*   Token to indicate the end of dialogue turn: `<end_of_turn>`

Here's an example dialogue:

```none
<start_of_turn>user
knock knock<end_of_turn>
<start_of_turn>model
who is there<end_of_turn>
<start_of_turn>user
Gemma<end_of_turn>
<start_of_turn>model
Gemma who?<end_of_turn>
```

The token `"<end_of_turn>\n"` is the turn separator, and the prompt prefix is
`"<start_of_turn>model\n"`. This means that if you'd like to prompt the model
with a question like, "What is Cramer's Rule?", you should instead feed the
model as follows:

```none
"<start_of_turn>user
What is Cramer's Rule?<end_of_turn>
<start_of_turn>model"
```

Note that if you want to finetune the pretrained Gemma models with your own
data, you can use any such schema for control tokens, as long as it's consistent
between your training and inference use cases.

## System instructions

Gemma's instruction-tuned models are designed to work with only two roles:
`user` and `model`. Therefore, the `system` role or a system turn is not
supported.

Instead of using a separate system role, provide system-level instructions
directly within the initial user prompt. The model instruction following
capabilities allow Gemma to interpret the instructions effectively. For example:

```none
<start_of_turn>user
Only reply like a pirate.

What is the answer to life the universe and everything?<end_of_turn>
<start_of_turn>model
Arrr, 'tis 42,<end_of_turn>
```

