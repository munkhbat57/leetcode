class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for oper in operations:
            if oper == 'X--' or oper =='--X':
                ans -=1
            else:
                ans +=1
        return ans