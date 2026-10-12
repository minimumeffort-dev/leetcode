"""LeetCode 49: Group Anagrams, using lowercase English letter counts."""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Group n words of maximum length k in O(n * (k + 26)) time."""
        groups: dict[tuple[int, ...], list[str]] = {}

        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord("a")] += 1

            # An immutable tuple of counts can be a dictionary key; a list cannot.
            key = tuple(counts)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
