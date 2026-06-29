# Speed-up Gemma 4 with Multi-Token Prediction

In Gemma 4, Multi-Token Prediction (MTP) is the specific architecture
used to enable highly efficient Speculative Decoding. Speculative
decoding is a technique to speed up inference in large language models.
Instead of relying solely on the large target model to generate tokens
autoregressively (generating one token at a time, where each new token
depends on the previous ones), a smaller, faster 'draft model' predicts
several tokens ahead. The target model then verifies these drafted
tokens in parallel. If the target model rejects a drafted token, it
still produces the correct token for that position (ensuring that step
is not wasted), and the draft model resumes predicting from that new
correct token.

Gemma 4 implements MTP by extending the base model with
this smaller, faster draft model. This draft model is not independent as
it shares the input embedding table with the target model and builds
directly upon its last-layer activations. This results in significant
decoding speedups while guaranteeing the exact
same quality as standard autoregressive generation, making these
checkpoints perfect for low-latency and on-device applications.

Speculative decoding works by drafting several tokens and verifying
them in a single forward pass. For dense models, the same weights are
used for every token, so verifying multiple drafted tokens adds minimal
overhead. Mixture of Experts (MoE) models like Gemma 4 26B A4B work
differently. Each token may activate different experts, so verifying
drafted tokens can require loading additional expert weights from
memory, offsetting the gains from drafting. At higher batch sizes,
there is typically more overlap in activated experts across sequences,
improving reuse of loaded weights. At batch size 1 this overlap is
limited, which is why the 26B A4B drafter may not yield speedups on
hardware platforms without good parallelism.

## MTP Enhancements

Gemma 4 introduces several enhancements to the standard speculative
decoding pipeline to improve the quality of drafted tokens and
efficiency:

* **Shared Input Embeddings**: The draft model shares the input embedding
  table with the target model.
* **Target Activations**: The draft model uses the activations from the
  last layer of the target model, concatenates them with the token
  embeddings, and down-projects them to the drafter model's dimension.
* **Efficient Embedder**: To avoid the expensive operation of predicting
  across the entire vocabulary, the model groups similar tokens into
  clusters. It first identifies the most likely clusters and then
  restricts its final calculations to only the tokens within those
  selected clusters (E2B and E4B only).
