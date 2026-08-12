class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = set(s)
        res = 0
        for letter in letters:
            replacement = k
            i = 0
            for j in range(len(s)):
                if s[j]!=letter:
                    replacement-=1
                while replacement<0:
                    if s[i]!=letter:
                        replacement+=1
                    i+=1
                res = max(res, (j-i)+1)
        return res
                

        