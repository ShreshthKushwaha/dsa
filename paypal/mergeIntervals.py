import heapq
class Solution:
    def merge(self, intervals):
        ans = []
        heapq.heapify(intervals)
        while len(intervals)>0:
            u,v = heapq.heappop(intervals)
            while len(intervals)>0 and intervals[0][0]<=v:
                updatedV = heapq.heappop(intervals)[1]
                v = max(updatedV,v)
            ans.append([u,v])
        return ans   