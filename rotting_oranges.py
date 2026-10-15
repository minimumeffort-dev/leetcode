"""LeetCode 994: Rotting Oranges, using multi-source breadth-first search.

Problem: https://leetcode.com/problems/rotting-oranges/
"""

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """Return minutes until all oranges rot, or -1 if some are unreachable.

        Time is O(rows * cols): scan every cell, then queue each orange at
        most once and check its four neighbours. deque operations take O(1)
        amortized time, and the level loops process each queued orange once.

        Extra space is O(rows * cols) for the queue in the worst case.
        Fresh oranges are changed from 1 to 2 in place when discovered, so
        the grid tracks visits without a separate set or input copy.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue: deque[tuple[int, int]] = deque()
        minutes = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    # All initially rotten oranges start spreading together.
                    queue.append((r, c))

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while queue and fresh > 0:
            # Freeze this minute's layer; newly rotten oranges wait until next time.
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row < 0
                        or col < 0
                        or row >= rows
                        or col >= cols
                        or grid[row][col] != 1
                    ):
                        continue

                    # Mark before queuing so two neighbours cannot count it twice.
                    grid[row][col] = 2
                    fresh -= 1
                    queue.append((row, col))

            minutes += 1

        # No fresh oranges initially means the loop was skipped and minutes is 0.
        return minutes if fresh == 0 else -1


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("All oranges eventually rot", [[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ("Unreachable fresh orange", [[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ("No fresh oranges", [[0, 2]], 0),
        ("Single fresh orange", [[1]], -1),
        ("Single rotten orange", [[2]], 0),
        ("Single empty cell", [[0]], 0),
        ("Spreading from both ends", [[2, 1, 1, 1, 2]], 2),
        ("Empty cell blocks the path", [[2, 0, 1]], -1),
        ("Empty grid", [], 0),
        ("Empty row", [[]], 0),
    ]

    for name, grid, expected in test_cases:
        found = solution.orangesRotting(grid)
        print(f"{name}: minutes={found}, expected={expected}")
        assert found == expected, name
