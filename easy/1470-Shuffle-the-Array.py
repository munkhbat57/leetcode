class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num1 = nums[:n]
        num2 = nums[n:]
        ans = [0] * n*2
        for i in range(len(num1)):
            ans[2*i] = num1[i]
        for i in range(len(num2)):
            ans[2*i+1] = num2[i]
        return ans
    