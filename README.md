# group-diagram-combination

Enumerate connected component-joining schemes between link factors.

## Installation

```bash
pip install group-diagram-combination
```

## Quick start

`from group_diagram_combination import main` then `main([2, 2, 1], 2)`.

PD codes are lists of four-entry crossings. Each arc label must occur exactly twice. Functions validate their inputs and do not mutate caller-owned PD-code lists unless explicitly documented.

## Development

Use Python 3.10 or newer for Python packages. Build distributions with `poetry build`. Run the package's tests or examples before publishing. C++ projects require a modern standards-compliant compiler.

## License

MIT. See `LICENSE`.
