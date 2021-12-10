class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for a in dic:
            n = dic[a]
            ans += n*(n-1)//2
        return ans
            
            