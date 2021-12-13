# Solution 1

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        mapping = {}
        
        for i, c in enumerate(keyboard):
            mapping[c] = i
        
        total_time = 0
        prev = 0
        
        for c in word:
            index = mapping[c]            
            total_time += abs(index - prev)            
            prev = index
            
        return total_time 

#Solution 2

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indexes=[]
        ans= 0
        for i in range(len(word)):
            ind = keyboard.index(word[i])
            indexes.append(ind)
            
        for i in range(len(indexes)):
            if i == 0:
                ans += indexes[i]
            else:
                ans += abs(indexes[i]-indexes[i-1])
        return ans