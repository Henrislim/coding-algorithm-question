class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        Sort the nums firstly
        -1 -1 0 0 1 1 1 1 2 2 2
        """
        res = []
        nums.sort()
        for i in range(0,len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[left]+nums[start]+nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -=1
                else:
                    res.append([nums[start], nums[left], nums[right]])
                    while left < right and (nums[left] == nums[left+1]):
                        left += 1
                    while left < right and (nums[right-1] == nums[right]):
                        right -= 1
                    left += 1
                    right -= 1
        return res

sol = Solution()
print sol.threeSum([-4,-3,-2,-2,-1,4,5,0,0,0,2,3,4,1,1,1,2,2]);
