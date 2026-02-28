# group_diagram_combination
Select several edges from a set of grouped nodes to form a grouped graph (e.g., bipartite graph, tripartite graph).

## Install

```bash
pip install group-diagram-combination
```

## Usage

```bash
from group_diagram_combination import main
print(main([2, 3, 4], 2))
```

## Problem Description
There are $K$ groups of nodes, where the $i$-th group contains $a_i$ distinct nodes (all nodes are unique). We need to connect exactly $M$ undirected edges in the graph such that:

1. Nodes within the same group cannot be connected to each other
2. The same edge cannot be selected twice

Calculate all valid solutions that satisfy the above constraints.

## Problem Input
Given a sequence $a_i$ of length $K$, and $M$.

## Problem Output
Output all valid solutions.

## Input Example
```txt
[[2, 2], 2]
```

## Output Example
```txt
[
    [[[1, 1], [2, 1]], [[1, 1], [2, 2]]],
    [[[1, 1], [2, 1]], [[1, 2], [2, 1]]],
    [[[1, 1], [2, 1]], [[1, 2], [2, 2]]],
    [[[1, 1], [2, 2]], [[1, 2], [2, 1]]],
    [[[1, 1], [2, 2]], [[1, 2], [2, 2]]],
    [[[1, 2], [2, 1]], [[1, 2], [2, 2]]],
]
```

**Note**: `[i, j]` denotes the $j$-th node in the $i$-th group. `[[x, y], [p, q]]` denotes an undirected edge between the $y$-th node in the $x$-th group and the $q$-th node in the $p$-th group. Both group numbers and node numbers start from 1.
