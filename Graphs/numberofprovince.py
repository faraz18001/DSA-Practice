isConnected=[[1,1,0],[1,1,0],[0,0,1]]

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
