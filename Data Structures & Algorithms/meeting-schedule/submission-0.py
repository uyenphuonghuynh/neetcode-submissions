"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        end = 0
        start = 0
        for i in intervals:
            s = i.start
            e = i.end
            if s < end:
                return False
            start = s
            end = e
        return True