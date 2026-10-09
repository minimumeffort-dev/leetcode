class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        i, j = 0, len(chars) - 1

        while i < j:
            while i < j and chars[i] not in vowels:
                i += 1
            while i < j and chars[j] not in vowels:
                j -= 1

            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1

        return "".join(chars)
