"""LeetCode 547: Number of Provinces, using breadth-first search.

Problem: https://leetcode.com/problems/number-of-provinces/
"""

from collections import deque


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        """Count connected groups of cities in an undirected graph.

        Time is O(n²): every city is queued once, and processing it scans
        its entire matrix row of n entries. The outer loop adds O(n) work.
        deque removes the oldest queued city in O(1) time.

        Extra space is O(n): the visited list has n entries, and the queue
        holds at most n cities. The input matrix is not copied or changed.
        """
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for city in range(n):
            if visited[city]:
                continue

            # Each new BFS explores one province that hasn't been counted.
            provinces += 1
            visited[city] = True
            queue = deque([city])

            while queue:
                current = queue.popleft()

                # The column index identifies a city; its value is 0 or 1.
                # Scan every column, including cities without a connection.
                for neighbour, connected in enumerate(isConnected[current]):
                    if connected and not visited[neighbour]:
                        # Mark on enqueue so cycles cannot queue it again.
                        visited[neighbour] = True
                        queue.append(neighbour)

        return provinces


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("Connected pair and isolated city", [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ("All isolated", [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
        ("Single city", [[1]], 1),
        (
            "Indirect connections",
            [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]],
            1,
        ),
        ("All directly connected", [[1] * 4 for _ in range(4)], 1),
        (
            "Two pairs",
            [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
            2,
        ),
        (
            "Cities grouped across different indices",
            [
                [1, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1],
            ],
            2,
        ),
        (
            "Cycle and isolated city",
            [[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1]],
            2,
        ),
    ]

    for name, connections, expected in test_cases:
        found = solution.findCircleNum(connections)
        print(f"{name}: provinces={found}, expected={expected}")
        assert found == expected, name
