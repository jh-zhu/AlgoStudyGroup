class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        while(low+1 < high):
            mid = int((low+high)/2)

            # situatioin1 peak
            if nums[mid-1] <= nums[mid] and nums[mid+1] <= nums[mid]:
                return mid

            # situation2 local low
            elif nums[mid-1] >=nums[mid] and nums[mid+1]>=nums[mid]:
                low = mid

            # situation3 decreasing
            elif nums[mid-1] >= nums[mid] and nums[mid+1] <=nums[mid]:
                high = mid

            # situation 4 increasing
            else:
                low = mid

        # check low and high
        if low==0 or high == len(nums)-1:
            return low if nums[low]>=nums[high] else high

        return low if nums[low-1] <=nums[low] and nums[low+1]<=nums[low] else high
