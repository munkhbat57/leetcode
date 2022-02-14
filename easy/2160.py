class Solution:
    def minimumSum(self, num: int) -> int:
        new = sorted(str(num),reverse = True)
        ans = int(new[0])+int(new[2])*10+ int(new[1])  +int(new[3])*10
        return ans