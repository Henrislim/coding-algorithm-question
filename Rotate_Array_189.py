class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums = nums[length-k:length]+nums[0:length-k]
        return nums

sol = Solution()
print sol.rotate([1,2],1)