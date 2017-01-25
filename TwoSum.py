class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index_1,nums_1 in enumerate(nums):
            nums_2_expected = target - nums_1
            for index_2,nums_2 in enumerate(nums):
                if (index_1 != index_2) & (nums_2_expected == nums_2):
                    return [index_1,index_2]

a = Solution()
my_result = a.twoSum([3,2,4],6)
print(my_result )