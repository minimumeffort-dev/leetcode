"""LeetCode 345: Reverse Vowels of a String."""


class Solution:
    def reverseVowels(self, s: str) -> str:
        """Swap vowels with two pointers; O(n) time and O(n) character storage.

        Each pointer moves inward without revisiting its previous positions,
        so the nested loops make O(n) moves in total. Creating and joining
        the character list also take O(n) time. That list and the result use
        O(n) space; the ten-vowel set has constant size.
        """
        vowels = set("aeiouAEIOU")
        chars = list(s)
        left, right = 0, len(chars) - 1

        while left < right:
            # Keep the bounds checks: a string may have no vowels at all.
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1

            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return "".join(chars)
