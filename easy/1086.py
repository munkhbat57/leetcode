class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(reverse=True)
        
        res = []
        curr = []
        idx = items[0][0]
        
        for i, val in items:
            if i == idx:
                if len(curr) < 5:
                    curr.append(val)
            else:
                res.append([idx, sum(curr) // len(curr)])
                curr = [val]
                idx = i
        
        res.append([idx, sum(curr) // len(curr)])
        
        res = res[::-1]
        
        return res