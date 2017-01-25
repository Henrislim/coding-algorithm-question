class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            if left == right:
                return left
            else:
                mid = (left+right)/2
                if nums[mid]<nums[mid+1]:
                    left = mid + 1
                else:
                    right = mid
        return mid
        """
        length = len(nums)
        if length == 1:
            return 0
        elif length == 2:
            if nums[1] < nums[0]:
                return 0
            else:
                return 1
        else:
            for key, value in enumerate(nums):
                if (key != 0) and (key != length - 1):
                    if value > nums[key-1] and value > nums[key+1]:
                        return key
                elif key == length - 1:
                    return 0
        """


sol = Solution()
print sol.findPeakElement([1,2,4,3,2,1])

