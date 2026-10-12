"""LeetCode 253: Meeting Rooms II."""

from heapq import heappop, heappush


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        """Sort the input in place; O(n log n) time and O(n) heap space."""
        intervals.sort(key=lambda interval: interval[0])

        # Keep the latest end time for each allocated room, including idle ones.
        end_times: list[int] = []
        for start, end in intervals:
            if end_times and end_times[0] <= start:
                heappop(end_times)  # Reuse the room that becomes free first.

            heappush(end_times, end)

        # Reusing a room keeps the heap size; it grows only when all rooms are busy.
        return len(end_times)
