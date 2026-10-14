"""LeetCode 323: Number of Connected Components in an Undirected Graph.

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """Count components using union by size and path halving.

        Creating the parent and size arrays costs O(n). Each of the E edges
        performs two finds and at most one merge. Union by size and path
        halving give O(n + E * alpha(n)) amortized total time. Here alpha is
        the inverse Ackermann function, which grows extremely slowly.

        Extra space is O(n) for the two arrays. Both helpers use constant
        call depth, and the input edges are neither copied nor changed.
        """
        parents = list(range(n))
        size = [1] * n

        def find(node: int) -> int:
            current = node
            while current != parents[current]:
                # Point to the grandparent, shortening future searches.
                parents[current] = parents[parents[current]]
                current = parents[current]
            return current

        def union(n1: int, n2: int) -> int:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                # An edge within one component does not reduce the count.
                return 0

            # Attach the smaller component's root to the larger one's root.
            # Only sizes at roots matter, since find() returns a root.
            if size[p2] > size[p1]:
                parents[p1] = p2
                size[p2] += size[p1]
            else:
                parents[p2] = p1
                size[p1] += size[p2]
            return 1

        # Initially every node is a separate component, including isolated nodes.
        components = n
        for n1, n2 in edges:
            components -= union(n1, n2)
        return components


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("Two groups", 5, [[0, 1], [1, 2], [3, 4]], 2),
        ("All isolated", 5, [], 5),
        ("Single node", 1, [], 1),
        ("Connected chain", 5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
        ("Cycle", 3, [[0, 1], [1, 2], [2, 0]], 1),
        ("Larger component is the second root", 4, [[0, 1], [2, 0]], 2),
        ("Cycle and separate pair", 5, [[0, 1], [1, 2], [2, 0], [3, 4]], 2),
        (
            "Edges eventually join every group",
            6,
            [[0, 1], [2, 3], [4, 5], [1, 3], [3, 5]],
            1,
        ),
    ]

    for name, n, edges, expected in test_cases:
        found = solution.countComponents(n, edges)
        print(f"{name}: components={found}, expected={expected}")
        assert found == expected, name
