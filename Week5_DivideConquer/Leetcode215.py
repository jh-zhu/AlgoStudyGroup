'''
Time 99.79%
Memory 80.39%

Using a priority queue for implememntation
'''


import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = nums[:k]
        heapq.heapify(hq)
        for i in range(k,len(nums)):
            if nums[i] > hq[0]:
                heapq.heappushpop(hq,nums[i])
        return hq[0]
