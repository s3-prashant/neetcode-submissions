class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l,r=0,len(numbers)-1
        # while l < r:
        #     total=numbers[l]+numbers[r]
        #     if total == target:
        #         return [l+1,r+1]
        #     elif total < target:
        #         l += 1
        #     else:
        #         r -= 1

        # #BF
        # n=len(numbers)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if numbers[i]+numbers[j] == target:
        #             return [i+1,j+1]
        # return []

        hashmap={}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            print(hashmap)
            if diff in hashmap:
                return [hashmap[diff]+1,i+1]
            hashmap[numbers[i]] = i
            
        