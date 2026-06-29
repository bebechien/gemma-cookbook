# Legacy Gemma setup

Note: This is only relevant for Gemma 3 and prior versions.

This page provides setup instructions for using Gemma in Colab. Some of the
instructions are applicable to other development environments as well.

## Get access to Gemma

Before using Gemma for the first time, you must request access to the
model through Kaggle. As part of the process, you'll have to use a Kaggle
account to accept the Gemma use policy and license terms.

If you don't already have a Kaggle account, you can register for one at
[kaggle.com](https://www.kaggle.com). Then complete the following steps:

1. Go to the [Gemma model card](https://www.kaggle.com/models/google/gemma)
   and select **Request Access**.
2. Complete the consent form and accept the terms and conditions.

## Select a Colab runtime

To complete a Colab tutorial, you must have a Colab runtime with sufficient
resources to run the Gemma model. To [get started](./get_started), you can
use a T4 GPU:

1. In the upper-right of the Colab window, select &#9662;
   (**Additional connection options**).
2. Select **Change runtime type**.
3. Under **Hardware accelerator**, select **T4 GPU**.

## Configure your API key

To use Gemma, you must provide your Kaggle username and a Kaggle API key. To
generate and configure these values, follow these steps:

1. To generate a Kaggle API key, go to the **Account** tab of your Kaggle [user
profile](https://www.kaggle.com/settings) and select **Create New Token**. This will trigger the download of a
`kaggle.json` file containing your API credentials.
2. Open `kaggle.json` in a text editor. The contents should look something like
   this:

   ```json
   {"username":"your_username","key":"012345678abcdef012345678abcdef1a"}
   ```
3. In Colab, select **Secrets** (🔑) and add your Kaggle username and Kaggle
   API key. Store your username under the name `KAGGLE_USERNAME` and your API
   key under the name `KAGGLE_KEY`.

   Note: Kaggle notebooks have a key storage feature under **Add-ons** >
   **Secrets**, along with instructions for accessing stored keys.

Now you're ready to complete the remaining setup steps in Colab. If you're
working through a Colab tutorial, go to Colab and set the environment variables.

Tip: As an alternative to setting environment variables, you can use `kagglehub`
to [authenticate](https://github.com/Kaggle/kagglehub?tab=readme-ov-file#authenticate).
