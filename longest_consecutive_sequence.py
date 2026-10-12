"""LeetCode 128: Longest Consecutive Sequence."""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """Count each run once; expected O(n) time and O(n) set space."""
        numbers = set(nums)
        longest = 0

        for number in numbers:
            # Only the first number of a run should start a forward scan.
            if number - 1 in numbers:
                continue

            length = 1
            while number + length in numbers:
                length += 1

            longest = max(longest, length)

        return longest
