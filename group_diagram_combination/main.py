import json

# 计算所有可能被使用的节点
def get_all_posible_node(A:list[int]) -> list:
    return [
        [raw_idx + 1, i]
        for raw_idx, a_i in enumerate(A)
        for i in range(1, a_i + 1)
    ]

# 计算所有可能被使用的边
def get_all_posible_edges(A:list[int]) -> list:
    all_node = get_all_posible_node(A)
    if len(all_node) != sum(A):
        raise AssertionError()
    return [
        [all_node[i], all_node[j]]
        for i in range(0, len(all_node))
        for j in range(i + 1, len(all_node))
        if all_node[i][0] != all_node[j][0]
    ]

# 使用 dfs 遍历所有方案
def dfs(arr:list[int], sol:list[list[int]], num_of_items:int, M:int) -> None:
    if len(arr) == M:
        sol.append(json.loads(json.dumps(arr)))
        return
    begin_val = 0 if len(arr) == 0 else arr[-1] + 1
    for val in range(begin_val, num_of_items):
        arr.append(val)
        dfs(arr, sol, num_of_items, M)
        arr.pop()

# 生成 combine 时编号从 0 开始
def get_all_m_combine(num_of_items:int, M:int) -> list:
    arr = []
    sol = []
    dfs(arr, sol, num_of_items, M)
    return sol

# 入口函数
def main(A:list[int], M:int) -> list:
    if len(A) < 1:
        raise AssertionError()
    for item in A:
        if item < 1:
            raise AssertionError()
    all_edges = get_all_posible_edges(A)
    all_m_combine = get_all_m_combine(len(all_edges), M)
    return [
        [all_edges[val] for val in item]
        for item in all_m_combine
    ]

if __name__ == "__main__":
    print(len(main([2, 2, 2, 2], 3)))
