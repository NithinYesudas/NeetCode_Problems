class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pal = []
        def dfs(i):
            if i >=len(s):
                res.append(pal.copy())
                return
            for j in range(i,len(s)):
                if isPal(s[i:j+1]):
                    pal.append(s[i:j+1])
                    dfs(j+1)
                    pal.pop()
        def isPal(word):
            l = 0
            r = len(word)-1
            while l<r:
                if word[l]!=word[r]:
                    return False
                l+=1
                r-=1
            return True
        dfs(0)
        return res