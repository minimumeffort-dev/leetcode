"""LeetCode 1071: Greatest Common Divisor of Strings."""

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Return the largest shared repeating pattern for two nonempty strings.

        Concatenation checks use O(n + m) time and extra space.
        """
        # Both concatenation orders match only when the strings share a pattern.
        if str1 + str2 != str2 + str1:
            return ""

        # A shared pattern's length must divide both string lengths.
        length = gcd(len(str1), len(str2))
        return str1[:length]
