"""LeetCode 49: Group Anagrams, using lowercase English letter counts."""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Group lowercase English words by their letter counts.

        Across n words containing C characters, counting costs O(C).
        Each word also creates, converts, and hashes a 26-entry counter,
        giving expected O(C + 26n) time, or O(C + n) for this fixed alphabet.
        Up to n keys of length 26 and n word references use O(n) extra space.
        """
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
