from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_map = Counter(t)
        n = len(t)
        l=0
        min_length = float("inf")
        res = ""
        
        for r in range(len(s)):
            
                
            freq_map[s[r]] = freq_map.get(s[r],0)-1
            if freq_map[s[r]]>=0:
                n-=1
            while n==0:
                min_length = min(min_length,(r-l)+1)
                if min_length == (r-l)+1:
                    res = s[l:r+1]

                if s[l] in freq_map:
                    freq_map[s[l]] = freq_map[s[l]]+1
                    if freq_map[s[l]]>0:
                        n+=1
                l+=1
        return res

        
                
            

        