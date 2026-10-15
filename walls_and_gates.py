"""LeetCode 286: Walls and Gates, using multi-source breadth-first search.

Problem: https://leetcode.com/problems/walls-and-gates/
"""

from collections import deque

INF = 2**31 - 1


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """Fill empty rooms with their distance to the nearest gate in place.

        Walls are -1, gates are 0, and undiscovered empty rooms are INF.
        Unreachable rooms keep INF. Starting BFS from every gate together
        ensures the first path to each room comes from a nearest gate.

        Time is O(rows * cols): scan every cell for gates, then queue each
        reachable cell once and check its four neighbours. deque operations
        take O(1) amortized time.

        Extra space is O(rows * cols) for the queue in the worst case,
        such as when every cell is a gate. The grid itself tracks discovery,
        so no separate visited set or copy of the input is needed.
        """
        if not rooms or not rooms[0]:
            return

        rows, cols = len(rooms), len(rooms[0])
        queue: deque[tuple[int, int]] = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    # Assign before queuing: this room is no longer undiscovered.
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            "Multiple gates and walls",
            [
                [INF, -1, 0, INF],
                [INF, INF, INF, -1],
                [INF, -1, INF, -1],
                [0, -1, INF, INF],
            ],
            [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]],
        ),
        ("All walls", [[-1, -1], [-1, -1]], [[-1, -1], [-1, -1]]),
        ("No gates", [[INF, INF], [INF, INF]], [[INF, INF], [INF, INF]]),
        ("Single gate", [[0]], [[0]]),
        ("Single unreachable room", [[INF]], [[INF]]),
        ("Room behind a wall", [[0, -1, INF]], [[0, -1, INF]]),
        ("Gates at both ends", [[0, INF, INF, INF, 0]], [[0, 1, 2, 1, 0]]),
        (
            "Single column with a wall",
            [[0], [INF], [-1], [INF]],
            [[0], [1], [-1], [INF]],
        ),
        ("Empty grid", [], []),
        ("Empty row", [[]], [[]]),
    ]

    for name, rooms, expected in test_cases:
        returned = solution.wallsAndGates(rooms)
        print(f"{name}: rooms={rooms}, expected={expected}")
        assert returned is None, name
        assert rooms == expected, name
