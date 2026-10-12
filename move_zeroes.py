"""LeetCode 283: Move Zeroes."""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """Move zeros in place, preserving nonzero order; O(n) time, O(1) space."""
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                # Positions before write already contain the nonzero prefix.
                if read != write:
                    nums[write], nums[read] = nums[read], nums[write]
                write += 1
