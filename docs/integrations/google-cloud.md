# Deploy Gemma with Google Cloud

The Google Cloud platform provides many options for deploying, serving,
and fine-tuning Gemma 4 open models, including the following:

-   [Vertex AI Model Garden](#vertex-ai-model-garden)
-   [Cloud Run](#cloud-run)
-   [Google Kubernetes Engine (GKE)](#google-kubernetes-engine-gke)
-   [Agent Development Kit (ADK)](#agent-development-kit-adk)
-   [Vertex AI Training Clusters (VTC)](#vertex-ai-training-clusters-vtc)
-   [MaxText](#maxtext)
-   [vLLM with TPUs](#vllm-with-tpus)
-   [Sovereign Cloud](#sovereign-cloud)

## Vertex AI Model Garden

[Vertex AI](https://cloud.google.com/vertex-ai) is a Google Cloud platform for
rapidly building and scaling machine learning projects.
Gemma 4 is available in
[Model Garden](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemma4),
a curated collection of models on Vertex AI.
You can test and deploy models directly from the console.

To learn more, refer to the following pages:

-   [Introduction to Vertex AI](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform):
    Get started with Vertex AI.
-   [Gemma with Vertex AI](https://cloud.google.com/vertex-ai/docs/generative-ai/open-models/use-gemma):
    Use Gemma open models with Vertex AI.

## Cloud Run

[Cloud Run](https://cloud.google.com/run) is a fully managed platform
to run your code or containers on top
of Google's highly scalable infrastructure.
[Deploy Gemma 4 on Cloud Run](https://docs.cloud.google.com/run/docs/run-gemma-on-cloud-run)
using GPUs for scale-to-zero, pay-per-use inference.

For larger mode sizes, [leverage advanced configurations](https://codelabs.developers.google.com/codelabs/cloud-run/cloud-run-gpu-rtx-pro-6000-gemma4-vllm)
with RTX 6000 Pro GPUs and Model Streaming.

## Google Kubernetes Engine (GKE)

[Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE)
is a managed Kubernetes service from Google Cloud.
[Run Gemma 4 on GKE](https://cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm)
for enterprise-grade container orchestration.
Use TPUs and GPUs to serve models with high throughput and low latency.

## Agent Development Kit (ADK)

Build and orchestrate AI agents with Gemma 4 and the [Agent Development Kit (ADK)](https://adk.dev/agents/models/google-gemma/).
Gemma 4's strong reasoning and function-calling capabilities make it ideal for
agentic workflows.

## Vertex AI Training Clusters (VTC)

[Fine-tune Gemma 4 using Vertex AI Training Clusters (VTC)](https://discuss.google.dev/t/end-to-end-guide-fine-tuning-and-serving-gemma-4-on-vertex-ai/345865).
VTC provides optimized infrastructure for large-scale training
and fine-tuning of open models.

## vLLM with TPUs

[Serve Gemma 4 on Google Cloud TPUs](https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html#cloud-tpu-deployment-via-docker)
for state-of-the-art serving performance.

## MaxText

Gemma 4 is supported in [MaxText](https://github.com/google/maxtext),
a high-performance,
arbitrary-sized JAX LLM implementation for Google Cloud TPUs.

## Sovereign Cloud

Gemma 4 is available on
[Sovereign Cloud](https://cloud.google.com/sovereign-cloud) solutions,
providing enhanced control and compliance for sensitive workloads.

