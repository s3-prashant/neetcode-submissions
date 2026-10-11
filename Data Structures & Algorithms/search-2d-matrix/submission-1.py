class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        for i in range(len(matrix)):
            l,r = 0,len(matrix[i])-1

            while l <= r:
                mid = (l+r)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    r -= 1
                else:
                    l += 1
        return False



        
        # for num in matrix:
        #     l,r=0,len(num)-1

        #     while l<=r:
        #         mid =(l+r)//2

        #         if num[mid] < target:
        #             l = mid+1
        #         elif num[mid] > target:
        #             r = mid-1
        #         else:
        #             return True
        #     # continue
        # return False