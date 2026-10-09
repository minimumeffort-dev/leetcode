from io import StringIO


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = StringIO()

        for a, b in zip(word1, word2):
            merged.write(a)
            merged.write(b)

        common = min(len(word1), len(word2))
        merged.write(word1[common:])
        merged.write(word2[common:])

        return merged.getvalue()
