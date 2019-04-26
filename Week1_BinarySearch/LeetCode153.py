class Solution:
    def findMin(self, nums: List[int]) -> int:
        low =0
        high = len(nums) -1 
        last = nums[-1]

        while(low+1 < high):
            mid = int((low+high)/2)

            if nums[mid] < last:
                high = mid
            else:
                low = mid

        # check low and high, the one less than the last number is what we want
        return nums[low] if nums[low] < last else nums[high]
