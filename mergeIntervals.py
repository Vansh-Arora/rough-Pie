class Solution:
    def merge(self,A,B):
        if B.start < A.start:
            A.start = B.start
        if B.end > A.end:
            A.end = B.end
        return A
    
    def insert(self, intervals, new_interval):
        if len(intervals) == 0:
            intervals.append(new_interval)
            return intervals
        elif new_interval.end < intervals[0].start:
            new = [new_interval]
            new.extend(intervals)
            return new
        elif new_interval.start > intervals[-1].end:
            intervals.append(new_interval)
            return intervals
        else:

            for i in intervals:
                if new_interval.start in range(i.start,(i.end)+1) or new_interval.end in range(i.start,(i.end)+1):
                    new_interval = self.merge(new_interval,i)


            i = 0
            temp = []
            while i < len(intervals) and intervals[i].start < new_interval.start:
                #ans.append(intervals[i])
                i += 1
            temp = intervals[i:]
            intervals = intervals[:i]
            i = 0
            intervals.append(new_interval)
            while i < len(temp):
                if temp[i].end > new_interval.end:
                    intervals.append(temp[i])
                i += 1
            return intervals
