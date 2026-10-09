class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Find the longest palindrome with Manacher's algorithm: O(n) time/space."""
        if not s:
            return ""

        # Separators let odd- and even-length palindromes use the same logic.
        transformed = "#" + "#".join(s) + "#"
        radii = [0] * len(transformed)
        center = right = 0
        best_start = best_length = 0

        for i in range(len(transformed)):
            if i < right:
                mirror = 2 * center - i
                # Reuse symmetry only within the palindrome we already know.
                radii[i] = min(right - i, radii[mirror])

            while (
                i - radii[i] - 1 >= 0
                and i + radii[i] + 1 < len(transformed)
                and transformed[i - radii[i] - 1]
                == transformed[i + radii[i] + 1]
            ):
                radii[i] += 1

            # Track the palindrome whose right edge reaches farthest.
            if i + radii[i] > right:
                center = i
                right = i + radii[i]

            if radii[i] > best_length:
                best_length = radii[i]
                best_start = (i - radii[i]) // 2

        return s[best_start : best_start + best_length]
