"""LeetCode 128: Longest Consecutive Sequence."""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """Count each run once; expected O(n) time and O(n) set space.

        Building the set costs expected O(n) time. Only run starts expand,
        so all inner loops together visit each distinct number once.
        Expected O(1) set checks keep the total linear, and the set stores
        at most n distinct values.
        """
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
