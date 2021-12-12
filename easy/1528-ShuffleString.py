#Solution 1
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        my_dict = {}
        ans = ''
        for i in range(len(indices)):
            my_dict[indices[i]] = s[i]
        dict(sorted(my_dict.items())).values()
        d = dict(sorted(my_dict.items()))
        for a in d.values():
            ans += a

        return ans

#Solution 2
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [None] * len(s)
        for i in range(len(s)):
            shuffled[indices[i]] = s[i]
            
        ans = ''.join(shuffled)
        return ans