class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        res.add(())
        nums.sort()
        def backtrack(i,path):
            if i >= len(nums):
                return
            path.append(nums[i])
            res.add(tuple(path))
            backtrack(i+1,path)
            path.pop()
            backtrack(i+1,path)
        backtrack(0,[])
        return [list(x) for x in res]
        