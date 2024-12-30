class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        st = 0
        end = len (nums) - 1
        while st <= end:
            mid = st + (end - st) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                st = mid + 1
        return st
        
