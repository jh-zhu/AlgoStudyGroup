def findFirst(nums,target):
    low = 0
    high = len(nums) - 1

    while(low +1 <high):
        mid = int((low+high)/2)
        if nums[mid] < target:
            low = mid+1
        elif nums[mid] >  target:
            high = mid -1
        else:
            high = mid
    if nums[low] == target:
        return low
    elif nums[high] == target:
        return high
    else:
        return -1

def findLast(nums, target):
    low = 0
    high = len(nums) -1
    while(low+1<high):
        mid = int((low+high)/2)
        if nums[mid] < target:
            low = mid+1
        elif nums[mid] > target:
            high = mid -1
        else:
            low = mid
    if nums[high] == target:
        return high
    elif nums[low] == target:
        return low
    else:
        return -1

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) ==1:
            return [0,0] if nums[0]==target else [-1,-1]

        left = findFirst(nums,target)
        right = findLast(nums,target)
        return [left,right]
                
