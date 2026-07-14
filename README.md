# group-diagram-combination

Enumerate connected ways to join selected components of several link factors.

## Installation

```bash
pip install group-diagram-combination
```

## Usage example

```python
from group_diagram_combination import main

# Three factors with 2, 2, and 1 components; choose two joins.
methods = main([2, 2, 1], 2)
print(methods[0])
```

## Algorithm

Each usable node is represented as `[factor_index, component_index]`. Candidate edges connect nodes from different factors. The algorithm enumerates edge subsets of the requested non-negative integer size and uses a disjoint-set union structure to reject subsets that do not connect every factor. For the composite-link generator the requested size is `n - 1`, so every accepted factor-level graph is a spanning tree.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

No external software is required.

## Development

Python 3.10 or newer is required. Run the exhaustive small-graph tests with:

```bash
python -m unittest discover -s tests -v
```

No PyPI publication is performed as part of repository maintenance.

## License

MIT. See `LICENSE`.

## Citation

If you use this repository in academic work, please cite it as:

```bibtex
@software{topologicalknotindexer_group_diagram_combination,
  author = {{GGN\_2015}},
  title = {{group\_diagram\_combination}},
  year = {2026},
  url = {https://github.com/TopologicalKnotIndexer/group_diagram_combination}
}
```
