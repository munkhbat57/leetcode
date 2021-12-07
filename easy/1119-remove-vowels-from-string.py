#Solution

class Solution:
    def removeVowels(self, s: str) -> str:
        list_to_eliminate = {'a', 'e', 'i', 'o', 'u'}
        new = []
        for char in s:
            if char not in list_to_eliminate:
                new.append(char)
        return ''.join(new)