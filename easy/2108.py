class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        i =0
        j =-1
        for word in words:
            if word == word[::-1]:
                return word
        return ""