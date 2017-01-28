class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        left = 0
        right = length - 1

        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left

sol = Solution()
nums = [3,3]
print sol.removeElement(nums,3)
print nums
print "Hello Chinese New Year of Rooster"
