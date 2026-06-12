class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left,right):
            count = 0
            while left>-1 and right<len(s) and s[right]==s[left]:
                count+=1
                right+=1
                left-=1
            return count
        res = 0
        for i in range(len(s)):
            res+=expand(i,i+1)
            res+=expand(i,i)
        return res

        
    