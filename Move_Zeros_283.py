class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        mark = 0

        for i in xrange(length):
            if nums[i] != 0:
                nums[mark] = nums[i]
                mark += 1
        for j in xrange(mark, length):
            nums[j] = 0

        """
        length = len(nums)
        i = 0
        zeros = 0
        while i+zeros < length:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                zeros +=1
            else:
                i += 1
        """