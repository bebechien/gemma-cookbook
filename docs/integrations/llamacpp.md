Project: /gemma/_project.yaml
Book: /gemma/_book.yaml

# Run Gemma with Llama.cpp

`llama.cpp` is a popular open-source library designed for efficient local
inference.

## Quick start

[Install](https://github.com/ggml-org/llama.cpp/blob/master/docs/install.md)
prebuilt version of llama.cpp

Example command:

```sh
# Download and run a model directly from Hugging Face
llama-cli -hf ggml-org/gemma-4-E2B-it-GGUF --prompt "Write a poem about the Kraken."

# Use System Prompt
llama-cli -hf ggml-org/gemma-4-E2B-it-GGUF -sys "You are Hong Gildong." -p "Who are you?"
```

To get started an run the model in a nice interface, you can start up a server
with:

```sh
llama-server -hf ggml-org/gemma-4-E2B-it-GGUF
```

This creates a server that lets you access your model either from an interface
(`http://localhost:8080`) or by accessing the OpenAI-endpoint
(`http://localhost:8080/v1`).

For more information and instructions on how to use `llama.cpp` with Gemma,
refer to the official repository:

[llama.cpp on GitHub](https://github.com/ggml-org/llama.cpp)
