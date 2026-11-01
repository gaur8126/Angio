# Angio

**Watch your model learn, from the inside.**

Angio attaches to your PyTorch training and shows, live in your browser:

- a map of your model with every layer coloured by health
- what each layer "sees" as training goes on
- a timeline you can rewind to replay how the model learned
- plain-language diagnoses: "learning rate too high", "dead activations in stage 3",
  "these images look mislabeled"

> Status: early development (v0). Not usable yet.

## Planned usage

```bash
pip install angio
```

```python
import angio

angio.attach(model, optimizer=optimizer)
# ... your normal training loop ...
```

```bash
angio ui        # opens http://localhost:8080
```

## Development

```bash
uv venv --python 3.12
uv pip install -e ".[dev,yolo]"
uv run pytest
```

See `docs/` for the vision, architecture and roadmap.