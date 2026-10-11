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

        for n in range(len(intervals)-1):
                n1= intervals[n]
                n2=intervals[n+1]
                if n1.end > n2.start:

                    return False
        return True