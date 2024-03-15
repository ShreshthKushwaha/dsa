class Solution:
    def countBattleships(self, board) -> int:


        def dfs(i,j):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return 
            if board[i][j]==".":
                return
            board[i][j]="."    
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        count = 0    

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="X":
                    dfs(i,j)
                    count+=1    
        return count    