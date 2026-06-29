Project: /gemma/_project.yaml
Book: /gemma/_book.yaml

# Run Gemma with MLX

MLX is an array framework for machine learning on Apple silicon.

## Quick start

[Install](https://ml-explore.github.io/mlx/build/html/install.html)
from the Python Package Index (PyPI)

```sh
pip install mlx mlx-lm mlx-vlm
```

Example command:

```sh
# Text Generation
mlx_lm.generate --model mlx-community/gemma-4-e2b-it-4bit --prompt "Who are you?"

# Vision Task
mlx_vlm.generate --model mlx-community/gemma-4-e2b-it-4bit --prompt "Describe this image." --image <path_to_image>
```

You can start the server with:

```sh
mlx_vlm.server --port 8080

# Preload a model at startup (Hugging Face repo or local path)
mlx_vlm.server --model mlx-community/gemma-4-e2b-it-4bit
```

This creates a server that lets you access your model with the OpenAI-compatible
endpoint (`http://localhost:8080/v1`).

For more information and instructions on how to use MLX with Gemma, refer to the
official repository:

- [MLX on GitHub](https://github.com/ml-explore/mlx)
- [MLX Community on Hugging Face](https://huggingface.co/mlx-community)
