from itertools import combinations


def get_all_posible_node(component_counts: list[int]) -> list[list[int]]:
    return [[group + 1, component] for group, count in enumerate(component_counts) for component in range(1, count + 1)]


def get_all_posible_edges(component_counts: list[int]) -> list[list[list[int]]]:
    nodes = get_all_posible_node(component_counts)
    return [[a, b] for a, b in combinations(nodes, 2) if a[0] != b[0]]


def get_all_m_combine(num_of_items: int, count: int) -> list[list[int]]:
    if count < 0 or count > num_of_items:
        return []
    return [list(items) for items in combinations(range(num_of_items), count)]


def connected(method: list, total_components: int) -> bool:
    if total_components <= 0:
        return False
    parent = list(range(total_components + 1))

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for left, right in method:
        a, b = find(left[0]), find(right[0])
        if a != b:
            parent[b] = a
    root = find(1)
    return all(find(group) == root for group in range(2, total_components + 1))


def select_all_connected(methods: list, total_components: int) -> list:
    return [method for method in methods if connected(method, total_components)]


def main(component_counts: list[int], edge_count: int) -> list:
    if not component_counts or any(isinstance(count, bool) or not isinstance(count, int) or count < 1 for count in component_counts):
        raise ValueError("component counts must be positive integers")
    edges = get_all_posible_edges(component_counts)
    return [
        [edges[index] for index in indices]
        for indices in combinations(range(len(edges)), edge_count)
        if connected([edges[index] for index in indices], len(component_counts))
    ]
