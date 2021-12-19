class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [start]
        ans = 0
        for i in range(1,n):
            arr.append(start+2*i)
        for i in range(len(arr)):
            ans = ans^arr[i]
        return ans