"""LeetCode 1971: Find if Path Exists in Graph, using breadth-first search.

Problem: https://leetcode.com/problems/find-if-path-exists-in-graph/
"""

from collections import deque


class Solution:
    def validPath(
        self,
        n: int,
        edges: list[list[int]],
        source: int,
        destination: int,
    ) -> bool:
        """Return whether two vertices are connected in an undirected graph.

        Vertices are numbered 0 through n-1. Creating the adjacency lists
        costs O(n+m), for m edges. Each vertex is queued at most once, and
        each edge is checked at most twice, giving O(n+m) total time.
        deque removes from the front in O(1) time; boolean indexing is O(1).

        The adjacency lists store n lists and 2m neighbour entries. The
        visited list and queue each use at most O(n) space, giving O(n+m)
        total working space. Identical endpoints take O(1) time and space
        because they return before any graph storage is allocated.
        """
        if source == destination:
            return True

        neighbours = [[] for _ in range(n)]
        for u, v in edges:
            # Each edge connects both ways.
            neighbours[u].append(v)
            neighbours[v].append(u)

        queue = deque([source])
        visited = [False] * n
        visited[source] = True

        while queue:
            # Process the oldest queued vertex, following BFS order.
            current = queue.popleft()
            if current == destination:
                return True

            for neighbour in neighbours[current]:
                if not visited[neighbour]:
                    # Mark on enqueue so cycles cannot queue this vertex again.
                    visited[neighbour] = True
                    queue.append(neighbour)

        # The source's whole connected component was explored without a match.
        return False


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("Triangle", 3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
        (
            "Disconnected components",
            6,
            [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]],
            0,
            5,
            False,
        ),
        ("Same vertex", 4, [[0, 1], [2, 3]], 2, 2, True),
        ("Single vertex", 1, [], 0, 0, True),
        ("No edges", 3, [], 0, 2, False),
        ("Isolated destination", 4, [[0, 1], [1, 2]], 0, 3, False),
        (
            "Cycle with a branch",
            5,
            [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4]],
            0,
            4,
            True,
        ),
        ("Reverse edge direction", 2, [[0, 1]], 1, 0, True),
    ]

    for name, n, edges, source, destination, expected in test_cases:
        found = solution.validPath(n, edges, source, destination)
        print(f"{name}: path_exists={found}, expected={expected}")
        assert found is expected, name
