"""LeetCode 1091: Shortest Path in Binary Matrix, using breadth-first search.

Problem: https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """Return the shortest clear path's cell count, or -1 if none exists.

        Expected time is O(n²): each cell is queued at most once, and each
        visit checks eight neighbours. Set operations take O(1) expected
        time, while deque appends and pops take O(1) amortized time.

        Extra space is O(n²) for the visited set and queue in the worst
        case. The input grid is left unchanged.
        """
        if not grid or not grid[0]:
            return -1

        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        # Path length counts cells, including the starting cell.
        queue: deque[tuple[int, int, int]] = deque([(0, 0, 1)])
        visited = {(0, 0)}
        directions = (
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, -1), (1, -1), (-1, 1),
        )

        while queue:
            r, c, length = queue.popleft()

            # BFS visits cells in increasing path length, so this is the shortest.
            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (
                    row < 0
                    or col < 0
                    or row >= n
                    or col >= n
                    or grid[row][col] != 0
                    or (row, col) in visited
                ):
                    continue

                # Check and mark before queuing to avoid invalid or repeated cells.
                visited.add((row, col))
                queue.append((row, col, length + 1))

        return -1


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("Diagonal path", [[0, 1], [1, 0]], 2),
        ("Path around obstacles", [[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ("Blocked start", [[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
        ("Blocked destination", [[0, 0], [0, 1]], -1),
        ("Single open cell", [[0]], 1),
        ("Single blocked cell", [[1]], -1),
        ("All cells open", [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 3),
        ("Barrier blocks every path", [[0, 0, 0], [1, 1, 1], [0, 0, 0]], -1),
        ("Empty grid", [], -1),
        ("Empty row", [[]], -1),
    ]

    for name, grid, expected in test_cases:
        original = [row.copy() for row in grid]
        found = solution.shortestPathBinaryMatrix(grid)
        print(f"{name}: length={found}, expected={expected}")
        assert found == expected, name
        assert grid == original, f"{name}: input grid was changed"
