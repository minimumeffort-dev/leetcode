"""LeetCode 1431: Kids With the Greatest Number of Candies."""


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """Check a nonempty list in O(n) time, with O(n) result space.

        max scans n values, then the comprehension checks n values again.
        Those two linear passes give O(n) time. The result stores n booleans;
        only the maximum and loop variables need constant working space.
        """
        max_candies = max(candies)
        # Tying the current maximum also counts as having the greatest amount.
        return [count + extraCandies >= max_candies for count in candies]
