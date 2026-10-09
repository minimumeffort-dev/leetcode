class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                if read != write:
                    nums[write], nums[read] = nums[read], nums[write]
                write += 1
