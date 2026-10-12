"""LeetCode 5: Longest Palindromic Substring, using brute force."""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Check mirrored characters without constructing a reversed string."""
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def longestPalindrome(self, s: str) -> str:
        """Brute force with length pruning: O(n^3) time, O(n) extra space."""
        if len(s) <= 1:
            return s

        best_length = 1
        best_substring = s[0]

        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                # Skip candidates that cannot beat the longest palindrome.
                if end - start <= best_length:
                    continue

                substring = s[start:end]
                if self.isPalindrome(substring):
                    best_length = end - start
                    best_substring = substring

        return best_substring
