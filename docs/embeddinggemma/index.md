# EmbeddingGemma model overview

:::{iframe} https://www.youtube.com/embed/Xu1X-J-r5Xk
:width: 100%
:::

EmbeddingGemma is a 308M parameter multilingual text embedding model based on
Gemma 3. It is optimized for use in everyday devices, such as phones, laptops,
and tablets. The model produces numerical representations of text to be used
for downstream tasks like information retrieval, semantic similarity
search, classification, and clustering.

EmbeddingGemma includes the following key features:

*   **Multilingual support**: Wide linguistic data understanding, trained in
    over 100 languages.
*   **Flexible output dimensions**: Customize your output dimensions from 768 to
    128 for speed and storage tradeoffs using Matryoshka Representation
    Learning (MRL).
*   **2K token context**: Substantial input context for processing text data and
    documents directly on your hardware.
*   **Storage efficient**: Run it on less than 200MB of RAM with quantization
*   **Low latency**: Generative embeddings in less than 22ms on EdgeTPU
   for fast and fluid applications.
*   **Offline and secure**: Generate embeddings of documents directly
   on your hardware, works without internet connection to keep
   sensitive data secure.

Tip: Deploy EmbeddingGemma with Gemma 3n to build contextually relevant
mobile-first Retrieval Augmented Generation (RAG) pipelines and chatbots.
See our
[quickstart RAG notebook][quickstart-rag-notebook]
to get started.

[quickstart-rag-notebook]: https://github.com/google-gemma/cookbook/blob/main/tutorials/RAG_with_EmbeddingGemma.ipynb

<a class="button" href="https://huggingface.co/collections/google/embeddinggemma-68b9ae3a72a82f0562a80dc4">Get it on Hugging Face</a>
<a class="button" href="https://www.kaggle.com/models/google/embeddinggemma">Get it on Kaggle</a>
<a class="button" href= "https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/embeddinggemma">Access it on Vertex</a>

As with other Gemma models, EmbeddingGemma is provided with open weights and
licensed for responsible [commercial use](/terms), allowing you to
fine tune and deploy it in your own projects and applications.

<a class="button button-primary" href="/gemma/docs/embeddinggemma/inference-embeddinggemma-with-sentence-transformers">Try EmbeddingGemma</a>
<a class="button button-primary" href="/gemma/docs/embeddinggemma/fine-tuning-embeddinggemma-with-sentence-transformers">Fine-tune EmbeddingGemma</a>
