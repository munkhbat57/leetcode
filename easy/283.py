class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        for i in range(n):
            k= n-i-1
            if nums[k] == 0:
                nums.pop(k)
                nums.append(0)
                