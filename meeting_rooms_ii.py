from heapq import heappop, heappush


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])

        end_times = []
        for start, end in intervals:
            if end_times and end_times[0] <= start:
                heappop(end_times)  # Reuse the room that becomes free first.

            heappush(end_times, end)

        return len(end_times)
