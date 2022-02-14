class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for sentence in sentences:
            words = sentence.split()
            if len (words) > ans:
                ans = len(words)
        return ans