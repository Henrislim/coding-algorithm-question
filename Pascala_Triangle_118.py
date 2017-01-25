class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        """
        result = [[]]*numRows
        for indx in range(0,numRows):
            if indx == 0:
                result[indx] = 1
            elif indx ==1:
                result[indx] = [1,1]
            else:
                array_tmp = [0]*(indx+1)
                array_tmp[0] = 1
                array_tmp[indx] = 1
                for k in range(1,indx):
                    array_tmp[k] = (result[indx-1])[k-1]+(result[indx-1])[k]
                result[indx] = array_tmp
        return result
        """
        result = [[1]*(i+1) for i in range(numRows)]
        for indx in range(0,numRows):
                for k in range(1,indx):
                    result[indx][k] = result[indx-1][k-1]+result[indx-1][k]
        return result

sol = Solution()
print sol.generate(6)
