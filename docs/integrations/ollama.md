# Run Gemma with Ollama

Running generative artificial intelligence (AI) models like Gemma can be
challenging without the right hardware. Open source frameworks such as
[llama.cpp][1] and [Ollama][2] make this easier by setting up a pre-configured
runtime environment that lets you to run versions of Gemma with less compute
resources. In fact, using llama.cpp and Ollama you can run versions of Gemma on
a laptop or other small computing device *without* a graphics processing unit
(GPU).

In order to run Gemma models with less compute resources, the llama.cpp and
Ollama frameworks use *quantized* versions of the models in the Georgi Gerganov
Unified Format (GGUF) model file format. These quantized models are modified to
process requests using smaller, less precise data. Using less precise data in
quantized models to process requests typically lowers the quality of the models
output, but with the benefit of also lowering the compute resource costs.

This guide describes how to set up and use Ollama to run Gemma to generate text
responses.

## Setup

This section describes how to set up Ollama and prepare a Gemma model instance
to respond to requests, including requesting model access, installing software,
and configuring a Gemma model in Ollama.

### Install Ollama

Before you can use Gemma with Ollama, you must download and install the Ollama
software on your computing device.

To download and install Ollama:

1.  Navigate to the download page: [https://ollama.com/download][3]
1.  Select your operating system, click the **Download** button or follow the
    instructions on the download page.
1.  Install the application by running the installer.
    *   **Windows:** Run the installer *.exe file and follow the instructions.
    *   **Mac:** Unpack the zip package and move the **Ollama** application
        folder to your **Applications** directory.
    *   **Linux:** Follow the instructions in bash script installer.
1.  Confirm that Ollama is installed by opening a terminal window and entering
    the following command:

    ollama --version

You should see a response similar to: `ollama version is #.#.##`. If you don't
get this result, make sure that the Ollama executable is added to your operating
system path.

### Configure Gemma in Ollama

The Ollama installation package does not include any models by default. You
download a model using the `pull` command.

To configure Gemma in Ollama:

1.  Download and configure the default Gemma 4 variant by opening a terminal
    window and entering the following command:

    ollama pull gemma4

1.  After completing the download you can confirm the model is available with
    the following command:

    ollama list

Models are specified as `<model_name>:<tag>`. For the Gemma 4, four sizes: E2B,
E4B, 26B and 31B parameters:

-   E2B Parameters `gemma4:e2b`
-   E4B Parameters `gemma4:e4b`
-   26B A4B Parameters `gemma4:26b`
-   31B Parameters `gemma4:31b`

You can find the available tags on the Ollama website, including [Gemma 4][4],
[Gemma 3n][5], [Gemma 3][6], [Gemma 2][7] and [Gemma][8].

## Generate responses

When you finish installing a Gemma model in Ollama, you can generate responses
immediately using Ollama's command line interface `run` command. Ollama also
configures a web service for accessing the model, which you can test using the
`curl` command.

To generate response from the command line:

-   In a terminal window, and entering the following command:

    ```sh
    ollama run gemma4 "roses are red"
    ```

-   Include the path to your image to use a visual input:

    ```sh
    ollama run gemma4 "caption this image /Users/$USER/Desktop/surprise.png"
    ```

To generate a response using the Ollama local web service:

-   In a terminal window, and entering the following command:

    ```sh
    curl http://localhost:11434/api/generate -d '{\
          "model": "gemma4",\
          "prompt":"roses are red"\
    }'
    ```

-   Include a list of base64-encoded images to use a visual input:

    ```sh
    curl http://localhost:11434/api/generate -d '{\
          "model": "gemma4",\
          "prompt":"caption this image",\
          "images":[...]\
    }'
    ```

## Tuned Gemma models

Ollama provides a set of official Gemma model variants for immediate use which
are quantized and saved in GGUF format. You can use your own tuned Gemma models
with Ollama by converting them to GGUF format. Ollama includes some functions to
convert tuned models from a Modelfile format to GGUF. For more information on
how to convert your tuned model to GGUF, see the Ollama [README][9].

## Next steps

Once you have Gemma running with Ollama, you can start experimenting and
building solutions with Gemma's generative AI capabilities. The command line
interface for Ollama can be useful for building scripting solutions. The Ollama
local web service interface can be useful for building experimental and
low-volume use applications.

-   Try integrating using the Ollama web service to create a locally-run
    [personal code assistant][10].
-   Learn how to [finetune a Gemma model][11].
-   Learn how to run Gemma with Ollama using [Google Cloud Run][12] services.
-   Learn about how to run Gemma with [Google Cloud][13].

[1]: https://github.com/ggerganov/llama.cpp
[2]: https://ollama.com/
[3]: https://ollama.com/download
[4]: https://ollama.com/library/gemma4/tags
[5]: https://ollama.com/library/gemma3n/tags
[6]: https://ollama.com/library/gemma3/tags
[7]: https://ollama.com/library/gemma2/tags
[8]: https://ollama.com/library/gemma/tags
[9]: https://github.com/ollama/ollama?tab=readme-ov-file#create-a-model
[10]: https://ai.google.dev/gemma/docs/personal-code-assistant
[11]: https://ai.google.dev/gemma/docs/core/lora_tuning
[12]: https://cloud.google.com/run/docs/tutorials/gpu-gemma-with-ollama
[13]: https://ai.google.dev/gemma/docs/integrations/google-cloud