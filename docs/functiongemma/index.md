# FunctionGemma model overview

:::{iframe} https://www.youtube.com/embed/-Tgc_9uYJLI
:width: 100%
:::

FunctionGemma is a specialized version of our Gemma 3 270M model tuned for
function calling. It is designed as a strong base for further training into
custom, fast, private, local agents that translate natural language into
executable API actions.

## When to choose FunctionGemma

FunctionGemma is the bridge between natural language and software execution. It
is the right tool if:

*   **You have a defined API surface:** Your application has a defined set of
    actions (e.g., smart home, media, navigation).
*   **You are ready to fine-tune:** You need the consistent, deterministic
    behavior that comes from fine-tuning on specific data, rather than the
    variability of zero-shot prompting.
*   **You prioritize local-first deployment:** Your application requires
    near-instant latency and total data privacy, running efficiently within the
    compute and battery limits of edge devices.
*   **You are building compound systems:** You need a lightweight edge model to
    handle local actions, allowing your system to process common commands
    on-device and only query larger models (like Gemma 3 27B) for more complex
    tasks.

<a class="button" href="https://huggingface.co/google/functiongemma-270m-it">Get it on Hugging Face</a>
<a class="button" href="https://www.kaggle.com/models/google/functiongemma">Get it on Kaggle</a>
<a class="button" href= "https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/functiongemma">Access it on Vertex</a>

As with other Gemma models, FunctionGemma is provided with open weights and
licensed for responsible [commercial use](/terms), allowing you to
fine tune and deploy it in your own projects and applications.

<a class="button button-primary" href="/gemma/docs/functiongemma/formatting-and-best-practices">Formatting and best practices</a>
<a class="button button-primary" href="/gemma/docs/functiongemma/function-calling-with-hf">Try FunctionGemma</a>

<a class="button button-primary" href="/gemma/docs/functiongemma/finetuning-with-functiongemma">Fine-tune FunctionGemma</a>
<a class="button button-primary" href="/gemma/docs/mobile-actions">Fine-tune the Mobile Actions demo</a>
