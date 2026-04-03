class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left= [1]*len(nums)
        right = [1]*len(nums)
        res= []

        for i in range(1,len(nums)):
            left[i] =left[i-1] *nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        return res