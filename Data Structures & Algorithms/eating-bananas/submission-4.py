class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        l,r = 1, max(piles)
        res=r

        while l <= r :
            total_time = 0
            mid = (l+r) // 2
            print(mid)

            for pile in piles:
                total_time += math.ceil((pile)/mid)

            if total_time <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1 
        return res




















        # l,r=1,max(piles)
        # res=r
        

        # while l<=r:
        #     k = (l+r)//2
        #     hours = 0
        #     for i in piles:
        #         hours += math.ceil((i)/k)
            
        #     if hours <= h:
        #         res = min(res,k)
        #         r= k-1
        #     else:
        #         l = k+1
        # return res