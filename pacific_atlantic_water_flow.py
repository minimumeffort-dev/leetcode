"""LeetCode 417: Pacific Atlantic Water Flow, using reverse-flow iterative DFS.

Problem: https://leetcode.com/problems/pacific-atlantic-water-flow/description/
"""


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """Return cells whose water can reach both oceans.

        Search backward from each ocean into cells of equal or greater
        height: water can flow from those cells back toward that ocean.

        Expected time is O(rows * cols). Each cell is pushed at most once
        per ocean, each visit checks four neighbours, and the final scan
        checks every cell. Set membership averages O(1).

        Extra space is O(rows * cols) for two visited sets and a DFS stack.
        The returned coordinates also take at most O(rows * cols) space.
        An explicit stack handles large plateaus without recursive calls.
        The input heights are neither copied nor changed.
        """
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific: set[tuple[int, int]] = set()
        atlantic: set[tuple[int, int]] = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(start_r: int, start_c: int, visited: set[tuple[int, int]]) -> None:
            if (start_r, start_c) in visited:
                return

            visited.add((start_r, start_c))
            stack = [(start_r, start_c)]
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        # Mark on push so equal-height cycles cannot add it twice.
                        visited.add((nr, nc))
                        stack.append((nr, nc))

        # The Pacific touches the top and left; the Atlantic the bottom and right.
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            "Mixed heights",
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ),
        ("Single cell", [[1]], [[0, 0]]),
        ("Single row", [[1, 3, 2, 4]], [[0, 0], [0, 1], [0, 2], [0, 3]]),
        ("Single column", [[1], [3], [2], [4]], [[0, 0], [1, 0], [2, 0], [3, 0]]),
        (
            "Flat plateau",
            [[2, 2, 2], [2, 2, 2]],
            [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]],
        ),
        (
            "Low center surrounded by higher ground",
            [[3, 3, 3], [3, 1, 3], [3, 3, 3]],
            [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],
        ),
        (
            "Heights increase toward the bottom right",
            [[1, 2, 3], [2, 3, 4]],
            [[0, 2], [1, 0], [1, 1], [1, 2]],
        ),
        (
            "Heights decrease toward the bottom right",
            [[4, 3, 2], [3, 2, 1]],
            [[0, 0], [0, 1], [0, 2], [1, 0]],
        ),
        ("Empty grid", [], []),
        ("Empty row", [[]], []),
    ]

    for name, heights, expected in test_cases:
        found = solution.pacificAtlantic(heights)
        print(f"{name}: cells={found}, expected={expected}")
        assert found == expected, name
