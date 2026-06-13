class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key= lambda x: x[0])
        final_intervals = []
        for i, item in enumerate(intervals):
            if i+1<len(intervals) and intervals[i+1][0]<=item[1]:
                intervals[i+1][0] = item[0]
                intervals[i+1][1] = max(item[1],intervals[i+1][1])
            else:
                final_intervals.append(item)
        return final_intervals
        