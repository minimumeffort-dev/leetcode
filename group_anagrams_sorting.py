"""LeetCode 49: Group Anagrams, using sorted letters."""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Group n words of maximum length k in O(n * k log k) time."""
        groups: dict[str, list[str]] = {}
        for word in strs:
            # Anagrams have the same letters once sorted, including duplicates.
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
