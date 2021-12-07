# Solution 1

class Solution1:
    def buildArray(self, nums: List[int]) -> List[int]:
        q = len(nums)
        for i,c in enumerate(nums):
            nums[i] += q * (nums[c] % q)
        for i,_ in enumerate(nums):
            nums[i] //= q
        return nums

# Solution 2

class Solution2:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans