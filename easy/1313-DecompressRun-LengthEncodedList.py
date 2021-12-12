class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freq = []
        val = []
        ans= []
        for i in range(len(nums)):
            if i % 2 ==0:
                freq.append(nums[i])
            else:
                val.append(nums[i])
        for i in range(len(val)):
            ans.extend([val[i]]*freq[i])
        return ans
                