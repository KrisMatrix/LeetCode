class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hash = {}
        hash[len(cost)] = 0
        hash[len(cost) + 1] = 0
        for i in range(len(cost)-1, -1, -1):
            hash[i] = min(hash[i+1] , hash[i+2]) + cost[i] 

        hash.pop(len(cost), None)
        hash.pop(len(cost)+1, None)
        
        if hash[0] < hash[1]:
            return hash[0]
        else:
            return hash[1]
        
        #value = [10,15,20,25]
        #index = [0, 1, 2, 3]
        
        #hash[index=3] = 0 +value[index=3] = 25 + 0
        #hash[index=2] = hash[ min(hash[index = 3],0) + value[index=2] = 20 + 0
        #hash[index=1] = hash[ min ( hash[index=2], hash[index=3])  ] + value[index = 1] = 20 + 15 = 35
        #hash[index=0] = hash[ min ( hash[index=1], hash[index=2])  ] + value[index = 0] = 20 + 10 = 30
        #hash[index = -1] = hash[ min ( hash[index=0], hash[index=1])  ] + value[index = -1] = 30 + 0 = 30
        
        #value = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        #index = [0,   1, 2, 3, 4,   5, 6, 7,   8, 9]
        
        #hash[index=9] = 0 + value[index=9] = 1
        #hash[index=8] = min(hash[9] + hash[10]) + value[index=8] = 0 + 100 = 100
        #hash[index=7] = min(hash[8] + hash[9]) + value[index=7] = 1 + 1 = 2
        #hash[index=6] = min(hash[7] + hash[8]) + value[index=6] = 2 + 1 = 3
        #hash[index=5] = min(hash[6] + hash[7]) + value[index=5] = 2 + 100 = 102
        #hash[index=4] = min(hash[5] + hash[6]) + value[index=4] = 3 + 1 = 4
        #hash[index=3] = min(hash[4] + hash[5]) + value[index=3] = 4 + 1 = 5
        #hash[index=2] = min(hash[3] + hash[4]) + value[index=2] = 4 + 1 = 5
        #hash[index=1] = min(hash[2] + hash[3]) + value[index=1] = 5 + 100 = 105
        #hash[index=0] = min(hash[1] + hash[2]) + value[index=0] = 5 + 1 = 6
    
