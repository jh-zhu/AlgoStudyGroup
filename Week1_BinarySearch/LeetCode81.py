class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False

        low = 0
        high = len(nums)-1

        while(low+ 1< high):

            # I looked up solutions for this while, can not debug for a long time here
            while(low+1 < high and nums[low] == nums[high]):
                low+=1



            mid = int((low+high)/2)
            if nums[mid] == target:
                return True



            if nums[mid] >= nums[low]:
                if nums[mid] >= target and nums[low] <= target:
                    high = mid
                else:
                    low = mid
            else:
                if nums[mid] <=target and nums[high] >=target:
                    low = mid
                else:
                    high = mid
        #check low and high
        return True if nums[low] == target or nums[high] == target else False
                
