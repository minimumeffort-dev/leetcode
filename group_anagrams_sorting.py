"""LeetCode 49: Group Anagrams, using sorted letters."""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Group words by a sorted-letter key.

        A k-letter word needs O(k log(k + 1)) sorting work, plus O(k) to
        join and hash its key. For n words of maximum length k, expected
        time is O(n * (1 + k log(k + 1))); the 1 covers empty words too.
        Stored keys use at most the total input character count C, and the
        groups hold n word references, giving O(C + n) extra space.
        """
        groups: dict[str, list[str]] = {}
        for word in strs:
            # Anagrams have the same letters once sorted, including duplicates.
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
