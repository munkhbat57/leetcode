class Solution:
    def sortSentence(self, s: str) -> str:
        
        lis = s.split()
        ans = [0]*len(lis)
        for word in lis:
            index = int(word[-1])-1
            word = word[:-1]
            ans[index] = word
        ans = ' '.join(ans)
        return ans
            
            