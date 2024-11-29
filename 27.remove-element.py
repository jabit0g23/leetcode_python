class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for a in nums[::-1]:     
            if a == val:
                nums.remove(val)     
        
