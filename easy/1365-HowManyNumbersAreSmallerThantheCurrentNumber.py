class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0]* len(nums)
        for i in range(len(nums)):
            for n in nums:
                if nums[i] > n:
                    ans[i]+=1
        return ans
                    