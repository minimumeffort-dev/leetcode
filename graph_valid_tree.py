"""LeetCode 261: Graph Valid Tree, using parent-aware iterative DFS.

Problem: https://leetcode.com/problems/graph-valid-tree/
Submission: https://leetcode.com/problems/graph-valid-tree/submissions/2172104907/
"""


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        """Check connectivity and cycles, returning True for an empty graph.

        Expected time is O(n+E): build the adjacency lists, then visit each
        node and adjacency entry at most once. Set membership averages O(1).
        For n > 0, E != n-1 is rejected in O(1) before allocating storage.

        Extra space is O(n+E) for adjacency lists, visited nodes and pending
        DFS work. Because E = n-1 after the early check, both bounds are O(n).
        An explicit stack handles long chains without recursive calls.
        The input edges are neither copied nor changed.
        """
        if not n:
            return True
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited: set[int] = set()
        # Each entry stores the same node and parent as the recursive DFS.
        stack = [(0, -1)]

        while stack:
            current, prev = stack.pop()
            if current in visited:
                # Reaching a node twice through different paths means a cycle.
                return False
            visited.add(current)

            for neighbor in adj[current]:
                if neighbor == prev:
                    # The reverse edge to our parent is not a cycle.
                    continue
                stack.append((neighbor, current))

        # A separate component may remain even if this DFS found no cycle.
        return len(visited) == n


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("Valid tree", 5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        ("Connected cycle", 3, [[0, 1], [1, 2], [2, 0]], False),
        ("Disconnected pairs", 4, [[0, 1], [2, 3]], False),
        ("Cycle and isolated node", 4, [[0, 1], [1, 2], [2, 0]], False),
        (
            "Cycle in an unreachable component",
            5,
            [[0, 1], [2, 3], [3, 4], [4, 2]],
            False,
        ),
        ("Single node", 1, [], True),
        ("Isolated nodes", 3, [], False),
        ("Chain", 5, [[0, 1], [1, 2], [2, 3], [3, 4]], True),
        ("Long chain", 2000, [[i, i + 1] for i in range(1999)], True),
        ("Empty graph", 0, [], True),
    ]

    for name, n, edges, expected in test_cases:
        found = solution.validTree(n, edges)
        print(f"{name}: valid_tree={found}, expected={expected}")
        assert found is expected, name
