class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i,path,currSum):
            if i>=len(nums) or currSum>target:
                return
            currSum+=nums[i]
            path.append(nums[i])
            if target == currSum:
                res.append(path.copy())
            backtrack(i,path,currSum)
            path.pop()
            backtrack(i+1,path,currSum-nums[i])
        backtrack(0,[],0)   
        return res

            
            
        