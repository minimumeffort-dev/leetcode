"""LeetCode 133: Clone Graph, using DFS and an original-to-copy dictionary.

Problem: https://leetcode.com/problems/clone-graph/
"""


class Node:
    """A graph node with its own list of neighbouring nodes."""

    def __init__(
        self, val: int = 0, neighbors: list["Node"] | None = None
    ) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        """Return a deep copy of the graph reachable from node.

        Expected time is O(V+E): each reachable node is copied once, each
        neighbour entry is processed once, and dictionary lookups average
        O(1). Undirected edges appear in two neighbour lists, which only
        doubles the edge work.

        Extra space is O(V) for the dictionary and recursion stack, which
        can reach V calls along a chain. The returned graph uses O(V+E)
        space for its new nodes and neighbour lists.
        """
        old_to_new: dict[Node, Node] = {}

        def dfs(node: Node) -> Node:
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            # Save it before recursing so a cycle reuses this same copy.
            old_to_new[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node) if node is not None else None


if __name__ == "__main__":
    def collect_nodes(start: Node | None) -> dict[int, Node]:
        """Collect nodes by their unique values to check the examples."""
        nodes: dict[int, Node] = {}
        pending = [start] if start is not None else []
        while pending:
            current = pending.pop()
            if current.val not in nodes:
                nodes[current.val] = current
                pending.extend(current.neighbors)
        return nodes

    solution = Solution()
    test_cases = [
        ("Four-node cycle", [[2, 4], [1, 3], [2, 4], [1, 3]]),
        ("Empty graph", []),
        ("Single node", [[]]),
        ("Two nodes", [[2], [1]]),
        ("Triangle", [[2, 3], [1, 3], [1, 2]]),
        ("Chain", [[2], [1, 3], [2, 4], [3]]),
        ("Star", [[2, 3, 4, 5], [1], [1], [1], [1]]),
        ("All directly connected", [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]]),
    ]

    for name, adjacency in test_cases:
        # LeetCode numbers these nodes from 1 through len(adjacency).
        originals = [Node(value) for value in range(1, len(adjacency) + 1)]
        for original, neighbor_values in zip(originals, adjacency):
            original.neighbors = [originals[value - 1] for value in neighbor_values]

        root = originals[0] if originals else None
        cloned_root = solution.cloneGraph(root)
        copies = collect_nodes(cloned_root)
        found = [
            [neighbor.val for neighbor in copies[value].neighbors]
            for value in range(1, len(copies) + 1)
        ]

        assert found == adjacency, name
        assert set(originals).isdisjoint(copies.values()), name
        for original in originals:
            assert copies[original.val].neighbors is not original.neighbors, name
        if root is None:
            assert cloned_root is None, name
        else:
            assert cloned_root is copies[root.val], name
        print(f"{name}: adjacency={found}, deep_copy=True")
