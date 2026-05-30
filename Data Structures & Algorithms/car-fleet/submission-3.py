class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mem = set()
        pairs = [[x,y] for x , y in zip(position,speed)]
        pairs.sort(reverse=True)
        res = 0
        recentTime = 0
        for pos, sp in pairs:
            timeNeeded = (target-pos)/sp
            if timeNeeded>recentTime:
                res+=1
                recentTime=timeNeeded
        
        return res
            
        