class Solution:
    def largestIsland(self, grid) -> int:
        

        id_areas = {}

        def isValid(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
                return False
            return True    



        def markArea(id,i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return 0
            if grid[i][j]!=1:
                return 0
            grid[i][j]=id
            top = markArea(id,i-1,j)
            bottom = markArea(id,i+1,j)
            left = markArea(id,i,j-1)
            right = markArea(id,i,j+1)


            return top+bottom+left+right+1
        id = -1    

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    total_area = markArea(id,i,j)
                    id_areas[id]= total_area
                    id-=1

        print (id_areas)
        ans = 0
        for k in id_areas:
            ans = max(ans,id_areas[k])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                uniqIds = set()
                if grid[i][j]==0:
                    directions = [(1,0),(0,1),(0,-1),(-1,0)]
                    for u,v in directions:
                        x = i+u
                        y = j+v
                        if isValid(x,y):
                            uniqIds.add(grid[x][y])
         

                area = 1            
                for id in list(uniqIds):
                    area+=id_areas[id]
                ans = max(ans,area)
        return ans            




                    




    












        