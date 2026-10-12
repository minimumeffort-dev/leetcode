"""LeetCode 1: Two Sum."""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Return two matching indices; expected O(n) time and O(n) space."""
        seen: dict[int, int] = {}
        for index, num in enumerate(nums):
            complement = target - num
            # Check before inserting so the same position cannot be used twice.
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        return []
