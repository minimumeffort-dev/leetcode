class Solution:
    def isPalindrome(self, s: str) -> bool:
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
        longest_sub = s[0]

        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                # Skip candidates that cannot beat the longest palindrome.
                if end - start <= best_length:
                    continue

                sub = s[start:end]
                if self.isPalindrome(sub):
                    best_length = end - start
                    longest_sub = sub

        return longest_sub
