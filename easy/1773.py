#Sol1
class Solution:

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        for item in items:
            if ruleKey=='type' and ruleValue==item[0]:
                ans +=1
            if ruleKey == "color" and ruleValue == item[1]:
                ans+=1
            if ruleKey == "name" and ruleValue == item[2]:
                ans+=1
        return ans

#Solution 2

key={
            "type":0,
            "color":1,
            "name":2
            }
        key_index=key[ruleKey]
        count=0
        for i in items:
            if i[key_index]==ruleValue:
                count+=1
        return count