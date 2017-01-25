class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        length = len(s)
        new_s = ['']*numRows
        index, step = 0, 1
        for value in s:
            new_s[index] += value
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return ''.join(new_s)

sol = Solution()
print sol.convert('ABCDEFGHIJKLMN',5)

"""
A   I
B H J
C G K
D F L N
E   M
"""

