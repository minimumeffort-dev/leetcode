class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numbers = set(nums)
        longest = 0

        for num in numbers:
            if num - 1 in numbers:
                continue

            length = 1
            while num + length in numbers:
                length += 1

            longest = max(longest, length)

        return longest
