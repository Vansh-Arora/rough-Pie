class Solution:
    def merge(self,A,B):
        if B.start < A.start:
            A.start = B.start
        if B.end > A.end:
            A.end = B.end
        return A
    ind = []
    def insert(self, intervals, new_interval):
        for i in intervals:
            if new_interval.start in range(i.start,(i.end)+1) or new_interval.end in range(i.start,(i.end)+1):
                new_interval = self.merge(new_interval,i)
        i = 0
        ans = []
        while i < len(intervals) and intervals[i].start < new_interval.start:
            ans.append(intervals[i])
            i += 1
        ans.append(new_interval)
        while i < len(intervals):
            if intervals[i].end > new_interval.end:
                ans.append(intervals[i])
            i += 1
        return ans
