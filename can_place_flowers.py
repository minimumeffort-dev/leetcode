class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        i = 0
        length = len(flowerbed)

        while i < length:
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == length - 1 or flowerbed[i + 1] == 0)
            ):
                n -= 1
                if n == 0:
                    return True
                i += 2
            else:
                i += 1

        return False
