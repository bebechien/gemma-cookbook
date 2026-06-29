# Run Gemma with LM Studio

[LM Studio][1] is a friendly yet powerful desktop application
for experimenting & developing with local AI models directly on your computer.
LM Studio supports Gemma models in both GGUF (llama.cpp) and MLX formats for
fast and efficient inference, completely locally on your machine.

## Setup

This section guides you through requesting model access, downloading and
installing LM Studio software, and loading a Gemma model into LM Studio.

### Download and Install LM Studio

Download the installer for macOS, Windows, or Linux from the [LM Studio
website][2].

After completing the download and running the installer, open the LM Studio
application and click around to familiarize yourself with the interface. To
download models, press Cmd + Shift + M on Mac, or Ctrl + Shift + M on PC.

## Download Gemma models to run locally

Gemma models are highly popular with local LLM users thanks to their minimal
memory footprint and powerful capabilities, including text generation,
instruction following, tool use, and in some cases image understanding. Explore
staff picked models within the app or in https://lmstudio.ai/models and find
Gemma models that fit your machine. You can also search and download Gemma
models from within the LM Studio app, or by using the lms CLI ([learn
more][3]).

**Using LM Studio's in-app model downloader**

1.  Open the LM Studio app and search for any model by presssing ⌘ + Shift + M
    on Mac, or Ctrl + Shift + M on PC.
2.  Search for "Gemma"
3.  Pick a result that looks interesting and LM Studio will suggest the suitable
    variant for your hardware.
4.  Click **Download**. After the download finishes, load the model to use it in
    a new chat.

## Advanced: Use your own converted GGUF Gemma model file

If you had converted a Gemma model to GGUF yourself, you can use LM Studio's CLI
`lms` to load your model into LM Studio.

1.  Use:

```bash
lms import <path/to/model.gguf>
```

2.  LM Studio will automatically detect the model and it will populate in the
    application under "My Models."
3.  Adjust context length and hardware settings as needed.

If `lms import` does not work automatically, you are still able to manually
import models into your LM Studio. Read more about LM Studio's model directory
structure at "[Import Models][4]".

Once the model has completed loading (as indicated by the progress bar), you may
start chatting away in LM Studio!

## Serve the model through LM Studio's server

**Serve via LM Studio's GUI**

In the LM Studio application, head to the Developer tab and then press Cmd /
Ctrl + L to open the model loader. Here you can view a list of downloaded models
and select one to load. LM Studio will by default select the load parameters
that optimizes model performance on your hardware.

**Serve via LM Studio's CLI**

If you prefer to work in the terminal, use LM Studio's CLI to interact with your
models. See a list of commands at "[lms][5]".

First, load a Gemma model you downloaded by running:

```bash
lms load <model_key>
``` You can find the model_key by first running
`lms ls` to list your locally downloaded models.

Next, turn on LM Studio's local API server by running:

```bash
lms server start
```

Now you're ready to go! Use LM Studio's REST APIs to use Gemma models
programmatically from your own code.

Learn more about how to do this
[https://lmstudio.ai/docs/developer][6].

## Appendix

**Getting a model from Hugging Face**

First, enable LM Studio under your [Local Apps
Settings][7] in Hugging Face.

On the model card, click the "Use this model" drop-down and select LM Studio.
This will run the model directly in LM Studio if you already have it, or show
you a download option if you don't.

[1]: https://lmstudio.ai
[2]: https://lmstudio.ai/download
[3]: https://lmstudio.ai/docs/cli/local-models/get
[4]: https://lmstudio.ai/docs/app/advanced/import-model
[5]: https://lmstudio.ai/docs/cli
[6]: https://lmstudio.ai/docs/developer
[7]: https://huggingface.co/settings/local-apps