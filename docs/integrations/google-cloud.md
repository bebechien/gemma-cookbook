# Deploy Gemma with Google Cloud

The Google Cloud platform provides many options for deploying, serving,
and fine-tuning Gemma 4 open models, including the following:

-   [Gemini Enterprise Agent Platform][1]
-   [Cloud Run][2]
-   [Google Kubernetes Engine (GKE)][3]
-   [Agent Development Kit (ADK)][4]
-   [Gemini Enterprise Agent Platform Training Clusters][5]
-   [MaxText][6]
-   [vLLM with TPUs][7]
-   [Sovereign Cloud][8]

## Gemini Enterprise Agent Platform

[Gemini Enterprise Agent Platform][9] is a Google Cloud platform for rapidly
building and scaling machine learning projects. Gemma 4 is available in [Model
Garden][10], a curated collection of models on Gemini Enterprise Agent Platform.
You can test and deploy models directly from the console.

To learn more, refer to the following pages:

-   [Agent Platform overview][11]: Get started with Gemini Enterprise Agent
    Platform.
-   [Gemma with Gemini Enterprise Agent Platform][9]: Use Gemma open models with
    Gemini Enterprise Agent Platform.

## Cloud Run

[Cloud Run][12] is a fully managed platform to run your code or containers on
top of Google's highly scalable infrastructure.
[Deploy Gemma 4 on Cloud Run][13] using GPUs for scale-to-zero, pay-per-use
inference.

For larger mode sizes, [leverage advanced configurations][14] with RTX 6000 Pro
GPUs and Model Streaming.

## Google Kubernetes Engine (GKE)

[Google Kubernetes Engine][15] (GKE) is a managed Kubernetes service from Google
Cloud. [Run Gemma 4 on GKE][16] for enterprise-grade container orchestration.
Use TPUs and GPUs to serve models with high throughput and low latency.

## Agent Development Kit (ADK)

Build and orchestrate AI agents with Gemma 4 and the [Agent Development Kit
(ADK)][17]. Gemma 4's strong reasoning and function-calling capabilities make it
ideal for agentic workflows.

## Gemini Enterprise Agent Platform Training Clusters

[Fine-tune Gemma 4 using Gemini Enterprise Agent Platform Training
Clusters][18]. Training Clusters provides optimized infrastructure for
large-scale training and fine-tuning of open models.

## vLLM with TPUs

[Serve Gemma 4 on Google Cloud TPUs][19] for state-of-the-art serving
performance.

## MaxText

Gemma 4 is supported in [MaxText][20], a high-performance, arbitrary-sized JAX
LLM implementation for Google Cloud TPUs.

## Sovereign Cloud

Gemma 4 is available on [Sovereign Cloud][21] solutions, providing enhanced
control and compliance for sensitive workloads.

[1]: integrations/google-cloud#gemini-enterprise-agent-platform
[2]: integrations/google-cloud#cloud-run
[3]: integrations/google-cloud#google-kubernetes-engine-gke
[4]: integrations/google-cloud#agent-development-kit-adk
[5]: integrations/google-cloud#gemini-enterprise-agent-platform-training-clusters
[6]: integrations/google-cloud#maxtext
[7]: integrations/google-cloud#vllm-with-tpus
[8]: integrations/google-cloud#sovereign-cloud
[9]: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-gemma
[10]: https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemma4
[11]: https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview
[12]: https://cloud.google.com/run
[13]: https://docs.cloud.google.com/run/docs/run-gemma-on-cloud-run
[14]: https://codelabs.developers.google.com/codelabs/cloud-run/cloud-run-gpu-rtx-pro-6000-gemma4-vllm
[15]: https://cloud.google.com/kubernetes-engine
[16]: https://cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm
[17]: https://adk.dev/agents/models/google-gemma/
[18]: https://discuss.google.dev/t/end-to-end-guide-fine-tuning-and-serving-gemma-4-on-vertex-ai/345865
[19]: https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html#cloud-tpu-deployment-via-docker
[20]: https://github.com/google/maxtext
[21]: https://cloud.google.com/sovereign-cloud