class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sor = sorted(nums)
        ans =[]
        for i in range(len(sor)):
            if sor[i] == target:
                ans.append(i)
                
        return ans