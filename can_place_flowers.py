"""LeetCode 605: Can Place Flowers."""


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """Scan the bed without modifying it; linear time, constant extra space.

        The index only moves forward, checking each plot at most once. Each
        check reads at most two neighbors, so time is O(number of plots).
        The counters use O(1) space, and no copy of the bed is created.
        """
        if n == 0:
            return True

        index = 0
        length = len(flowerbed)

        while index < length:
            if (
                flowerbed[index] == 0
                and (index == 0 or flowerbed[index - 1] == 0)
                and (index == length - 1 or flowerbed[index + 1] == 0)
            ):
                n -= 1
                if n == 0:
                    return True
                # Skip the plot blocked by this placement instead of mutating it.
                index += 2
            else:
                index += 1

        return False
