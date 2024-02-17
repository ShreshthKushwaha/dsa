class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:


        if sum(gas)<sum(cost):
            return -1
        
        curr =0 
        start = 0
      
        ##as soultion is guaranteed to be unique..and we have checked form 0 to ansStart...we would have already checked all others (0...i...)

        for i in range(len(gas)):
            curr+=(gas[i]-cost[i])

            if curr<0:
                start = i+1
                curr = 0
        return start    