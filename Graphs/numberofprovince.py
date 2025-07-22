class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row,cols=len(arr),len(arr[0])
        def dfs(i,j):
        if i < 0 or i >= len(isConnected) or j < 0 or j >= len(isConnected[0]):

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)  #
            dfs(i, j+1)



        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==1:
                    dfs(i,j)
















        """adj_list={}
        for i in range(len(isConnected)):
            adj_list[i]=[]
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    adj_list[i].append(j)"""
