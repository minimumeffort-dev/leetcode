"""LeetCode 5: Longest Palindromic Substring, using brute force."""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Check mirrored characters in O(k) time and O(1) space for length k.

        At most k // 2 pairs are compared, using only two pointer indices.
        """
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def longestPalindrome(self, s: str) -> str:
        """Brute force with length pruning: O(n^3) time, O(n) extra space.

        There are O(n^2) candidate substrings. Copying a slice and checking
        it can each cost O(n), giving O(n^3) worst-case time. Pruning skips
        some candidates but does not change that worst-case bound. Only a
        current candidate and best substring are retained, using O(n) space.
        """
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
