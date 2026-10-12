"""LeetCode 5: Longest Palindromic Substring, using center expansion."""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Expand around centers: O(n^2) time, O(1) space excluding the result."""
        best_start = best_length = 0

        for center in range(len(s)):
            # Check a character center (odd) and a gap center (even).
            for left, right in ((center, center), (center, center + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    length = right - left + 1
                    if length > best_length:
                        best_start = left
                        best_length = length

                    left -= 1
                    right += 1

        return s[best_start : best_start + best_length]
