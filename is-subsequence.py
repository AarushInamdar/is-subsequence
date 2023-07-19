class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = 0
        res= []
        if len(s) == 0:
            return True
        else:
            for char in t:
                if char == s[n]:
                    res.append(char)
                    if len(res) == len(s):
                        return True
                    n += 1
            
        return len(res) == len(s)