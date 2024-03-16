class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:

        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        visit = set()    

        def isValid(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return False
            if (i,j) in visit:
                return False
            return True        


        q = []

        q.append((0,0,1))

        while len(q)!=0:

            i,j,l = q.pop(0)
            visit.add((i,j))
            if i==len(grid)-1 and j==len(grid[0])-1:
                return l

            directions = [(0,1),(1,0),(1,1),(-1,-1),(1,-1),(-1,1),(-1,0),(0,-1)]
            for u,v in directions:
                x = i+u
                y = j+v
                if isValid(x,y) and grid[x][y]==0:
                    visit.add((x,y))
                    q.append((x,y,l+1))
        return -1            
            




        