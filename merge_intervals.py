"""LeetCode 56: Merge Intervals."""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """Sort the input in place and merge; O(n log n) time, O(n) space.

        Sorting n intervals costs O(n log n); the following scan performs
        constant work per interval, adding O(n). The result can contain
        n intervals, and Python's sort can also use O(n) temporary storage.
        """
        intervals.sort(key=lambda interval: interval[0])

        merged: list[list[int]] = []
        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                # An interval contained inside the last one must not shrink it.
                merged[-1][1] = max(merged[-1][1], end)

        return merged
