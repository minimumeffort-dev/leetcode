"""LeetCode 1768: Merge Strings Alternately."""

from io import StringIO


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """Build the merged string in O(n + m) time and buffer space.

        For word lengths n and m, zip writes the paired characters and the
        tail writes handle the rest: n + m characters in total. The buffer
        and returned string hold that many characters, using O(n + m) space.
        """
        merged = StringIO()

        for first_char, second_char in zip(word1, word2):
            merged.write(first_char)
            merged.write(second_char)

        # zip stops at the shorter word; at most one of these tails is nonempty.
        common = min(len(word1), len(word2))
        merged.write(word1[common:])
        merged.write(word2[common:])

        return merged.getvalue()
