class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        letters = {}
        
        for i in s:
            if i not in letters:
                letters[i] = 1
                
            else:
                letters[i] += 1
                
        res = 0
        odd = 0
        
        if len(letters) == 1:
            return letters[s[0]]
        
        for j in letters.values():
            if j > 1:
                if j % 2 == 0:
                    res += j
                else:
                    res += (j-1)
                    odd += 1
            else:
                odd += 1
                
        if odd > 0:
            res += 1
                
        return res
        
