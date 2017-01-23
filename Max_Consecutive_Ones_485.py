class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        length = len(nums)
        temp_num = 0
        temp_num_next = 0
        for key,num in enumerate(nums):
            if num == 1:
                temp_num += 1
            if (num == 0) or (key == length-1):
                if temp_num_next <= temp_num:
                    temp_num_next = temp_num
                temp_num = 0
        return temp_num_next

sol = Solution()
print(sol.findMaxConsecutiveOnes([1,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,1]))

