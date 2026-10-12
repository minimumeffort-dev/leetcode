"""LeetCode 480: Sliding Window Median, using two heaps.

Problem: https://leetcode.com/problems/sliding-window-median/
"""

from heapq import heapify, heappop, heappush


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        """Return window medians in O(n log(k+1)) time and O(k) working space.

        Assume 1 <= k <= len(nums). The smaller half has the same number of
        live entries as the larger half, or one extra, so their tops expose
        the middle values. Entries include indices to distinguish duplicates.

        Each update inserts one entry and makes a constant number of heap
        transfers. Expired entries are removed when they reach a heap's top.
        Periodic cleanup keeps the heaps at O(k) entries, so the O(n) total
        pushes/pops cost O(n log(k+1)). Cleanup uses O(k) filtering/heapify
        after at least k further insertions, adding O(n) total cleanup work.
        Thus each slide costs O(log(k+1)) amortized, rather than shifting a list.

        The heaps and live-index map use O(k) space. The returned list stores
        n-k+1 medians. nums is read without changing it.
        """
        # heapq is a min-heap. Negating values makes small act as a max-heap.
        small: list[tuple[int, int]] = []
        large: list[tuple[int, int]] = []

        # True means an active index is in small; False means it is in large.
        in_small: dict[int, bool] = {}
        small_size = large_size = 0  # Count live entries, ignoring expired ones.
        window_start = 0
        medians: list[float] = []

        def prune(heap: list[tuple[int, int]]) -> None:
            """Pop expired entries once they become accessible at the top."""
            while heap and heap[0][1] < window_start:
                heappop(heap)

        def rebalance() -> None:
            """Keep small's live size equal to large's, or one larger."""
            nonlocal small_size, large_size

            while small_size > large_size + 1:
                negative_value, index = heappop(small)
                heappush(large, (-negative_value, index))
                in_small[index] = False
                small_size -= 1
                large_size += 1
                prune(small)

            while small_size < large_size:
                value, index = heappop(large)
                heappush(small, (-value, index))
                in_small[index] = True
                large_size -= 1
                small_size += 1
                prune(large)

        for index, value in enumerate(nums):
            if not small or value <= -small[0][0]:
                heappush(small, (-value, index))
                in_small[index] = True
                small_size += 1
            else:
                heappush(large, (value, index))
                in_small[index] = False
                large_size += 1

            if index >= k:
                window_start = index - k + 1

                # Forget the outgoing index immediately, even if it is buried.
                # Looking up its heap by index avoids ambiguity with equal values.
                if in_small.pop(index - k):
                    small_size -= 1
                else:
                    large_size -= 1

            # Clean the tops before comparing sizes or moving entries.
            prune(small)
            prune(large)
            rebalance()

            # Buried expired entries can accumulate in increasing/decreasing input.
            # Filter and heapify occasionally so the heaps contain O(k) entries.
            if len(small) + len(large) > 2 * k:
                for heap in (small, large):
                    heap[:] = [entry for entry in heap if entry[1] >= window_start]
                    heapify(heap)

            if index >= k - 1:
                if k % 2 == 0:
                    medians.append((-small[0][0] + large[0][0]) / 2)
                else:
                    medians.append(float(-small[0][0]))

        return medians


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            "LeetCode example",
            [1, 3, -1, -3, 5, 3, 6, 7],
            3,
            [1.0, -1.0, -1.0, 3.0, 5.0, 6.0],
        ),
        ("Even window", [1, 4, 2, 3], 2, [2.5, 3.0, 2.5]),
        ("Duplicates", [2, 2, 2, 2], 3, [2.0, 2.0]),
        ("Window of one", [3, -1, 2], 1, [3.0, -1.0, 2.0]),
        ("Whole array", [3, 1, 2, 4], 4, [2.5]),
        ("Integer limits", [-2**31, 2**31 - 1], 2, [-0.5]),
        ("Increasing input", list(range(10)), 3, [float(i) for i in range(1, 9)]),
        (
            "Decreasing input",
            list(range(9, -1, -1)),
            3,
            [float(i) for i in range(8, 0, -1)],
        ),
    ]

    for name, nums, k, expected in test_cases:
        medians = solution.medianSlidingWindow(nums, k)
        print(f"{name}: medians={medians}, expected={expected}")
        assert medians == expected, name
