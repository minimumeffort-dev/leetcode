"""LeetCode 200: Number of Islands, using breadth-first search.

Problem: https://leetcode.com/problems/number-of-islands/
"""

from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """Count islands connected horizontally or vertically.

        Expected time is O(rows * cols): the outer loops scan every cell,
        and BFS queues each land cell once and checks its four neighbours.
        Set membership averages O(1), and deque.popleft() takes O(1).

        Extra space is O(rows * cols) in the worst case for the visited set
        and queue. The input grid is neither copied nor changed.
        """
        islands = 0
        if not grid:
            return islands

        rows, cols = len(grid), len(grid[0])
        visited: set[tuple[int, int]] = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def bfs(row: int, col: int) -> None:
            queue = deque([(row, col)])
            visited.add((row, col))

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    # Start each direction from the same current cell.
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in visited
                    ):
                        # Mark on enqueue so each land cell is queued once.
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # This BFS marks one entire island before scanning resumes.
                    bfs(r, c)
                    islands += 1

        return islands


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("One island", ["11110", "11010", "11000", "00000"], 1),
        ("Three islands", ["11000", "11000", "00100", "00011"], 3),
        ("Requires moving upward", ["101", "111"], 1),
        ("Requires moving left", ["011", "110"], 1),
        ("Diagonal cells are separate", ["10", "01"], 2),
        ("All water", ["000", "000"], 0),
        ("Single land cell", ["1"], 1),
        ("Single row", ["1100110"], 2),
        ("Single column", ["1", "1", "0", "1"], 2),
        ("Empty grid", [], 0),
        ("Empty row", [""], 0),
    ]

    for name, row_strings, expected in test_cases:
        # Convert the compact example rows to LeetCode's list-of-lists format.
        grid = [list(row) for row in row_strings]
        found = solution.numIslands(grid)
        print(f"{name}: islands={found}, expected={expected}")
        assert found == expected, name
