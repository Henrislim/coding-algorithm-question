class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        left = 0
        right = length-1
        while left < right:
            summation = numbers[left]+numbers[right]
            if summation < target:
                left += 1
            elif summation > target:
                right -= 1
            else:
                return [left, right]
        return 0

sol = Solution()
print sol.twoSum([2,3,4],6)