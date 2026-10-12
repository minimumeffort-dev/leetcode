"""LeetCode 480: Sliding Window Median, using one sorted list.

Problem: https://leetcode.com/problems/sliding-window-median/

This version reuses the sorted window; list shifts still cost O(k) per slide.
"""

from bisect import bisect_left, insort


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        """Return the median of each window, assuming 1 <= k <= len(nums).

        Sorting the first window costs O(k log k). Each of the n-k updates
        uses O(log k) searches, but removal and insertion can shift O(k)
        elements. Reading the middle values and appending each median costs
        amortized O(1), giving O(k log(k+1) + (n-k)k) total worst-case time.
        The log(k+1) form also covers a window of size one.

        The window and sorting workspace use O(k) extra space. The returned
        list stores n-k+1 medians. nums is read without changing it.
        """
        medians = []
        j = 0

        # Sort the first window once.
        window = sorted(nums[:k])

        while j + k <= len(nums):
            if k % 2 == 0:
                medians.append((window[k // 2] + window[k // 2 - 1]) / 2)
            else:
                medians.append(window[k // 2])

            j += 1

            # Update only if another window exists.
            if j + k <= len(nums):
                outgoing = nums[j - 1]
                incoming = nums[j + k - 1]

                # Remove one occurrence, including when duplicates are present.
                window.pop(bisect_left(window, outgoing))
                insort(window, incoming)

        return medians


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            "LeetCode example",
            [1, 3, -1, -3, 5, 3, 6, 7],
            3,
            [1.0, -1.0, -1.0, 3.0, 5.0, 6.0],
        ),
        ("Even window", [1, 4, 2, 3], 2, [2.5, 3.0, 2.5]),
        ("Duplicates", [2, 2, 2, 2], 3, [2.0, 2.0]),
        ("Window of one", [3, -1, 2], 1, [3.0, -1.0, 2.0]),
        ("Whole array", [3, 1, 2, 4], 4, [2.5]),
        ("Integer limits", [-2**31, 2**31 - 1], 2, [-0.5]),
    ]

    for name, nums, k, expected in test_cases:
        medians = solution.medianSlidingWindow(nums, k)
        print(f"{name}: medians={medians}, expected={expected}")
        assert medians == expected, name
