class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:      
        while(len(stones) > 1):
            stones.sort(reverse=True)
            x = stones.pop(0)
            y = stones.pop(0)
            if x != y:
                stones.insert(0, abs(x-y))
                
        if len(stones):
            return stones[0]
        else:
            return 0
