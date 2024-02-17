class Solution:
    def minCost(self, houses, cost, m: int, n: int, target: int) -> int:
        mem = {}
        def paint(i,nbrs,prevColor):
            if i >=len(houses) and nbrs==0:
                return 0
            if i>=len(houses):
                return 2**31    
            if nbrs<0:
                return 2**31
            if (i,nbrs,prevColor) in mem:
                return mem[(i,nbrs,prevColor)]    

            temp_ans = 2**31
            if houses[i]!=0:
                if i==0:
                    mem[(i,nbrs,prevColor)] = paint(i+1,nbrs-1,houses[i]-1)

                else:
                    if houses[i]-1==prevColor:
                        mem[(i,nbrs,prevColor)] = paint(i+1,nbrs,houses[i]-1)
                    else:
                        mem[(i,nbrs,prevColor)] = paint(i+1,nbrs-1,houses[i]-1) 
                return mem[(i,nbrs,prevColor)]         



            if i==0:
                for color_index in range(len(cost[i])):
                    temp_ans = min(temp_ans,cost[i][color_index]+paint(i+1,nbrs-1,color_index))
            else:
                for color_index in range(len(cost[i])):
                    if color_index==prevColor:
                        temp_ans = min(temp_ans,cost[i][color_index]+paint(i+1,nbrs,color_index))
                    else:
                        temp_ans = min(temp_ans,cost[i][color_index]+paint(i+1,nbrs-1,color_index))
            mem[(i,nbrs,prevColor)] = temp_ans            
            return temp_ans   
        final_ans =  paint(0,target,None)            
        if final_ans>=2**31:
            return -1
        return final_ans    



                 



        