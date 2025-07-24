
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
word = "ABCCED"

def solution(board,word):
    rows = len(board)
    cols = len(board[0])

    def dfs(square,i,j):
        if 0<=i<rows and 0<=j<cols:
            if square[i][j] in word:
                return
            else:
                dfs(square,i-1,j)
                dfs(square,i+1,j)
                dfs(square,i,j-1)
                dfs(square,i,j+1)


    visited=set()
    for i in range(rows):
        for j in range(cols):
            if board[i][j] in word and board[i][j] not in visited:
                visited.add(board[i][j])
                dfs(board[i][j],i,j)

def word_search(word,board):
    def dfs(board,i,j):

        rows=len(board)
        cols=len(board)
        vistied=set()
        stack=[(i,j)]

        while len(stack)!=0:
            for row in range(rows):
                for col in range(cols):
                    if board[i][j] in word and board[i][j] not in vistied:
                        vistied.add(board[i][j])
                        stack.append((i-1, j))  # Up
                        stack.append((i+1, j))  # Down
                        stack.append((i, j-1))  # Left
                        stack.append((i, j+1))

        return stack



def word_search(word, board):
    if not board or not board[0]:
        return False

    rows = len(board)
    cols = len(board[0])

    def dfs(start_i, start_j):
        visited = set()
        stack = [(start_i, start_j, 0)]  # Add word_index to track position in word

        while stack:  # Fix: use while stack instead of len(stack)!=0
            i, j, word_idx = stack.pop()

            # Check bounds
            if i < 0 or i >= rows or j < 0 or j >= cols:
                continue

            # Check if already visited or character doesn't match
            if (i, j) in visited or board[i][j] != word[word_idx]:
                continue

            # If we found the whole word
            if word_idx == len(word) - 1:
                return True

            # Mark as visited
            visited.add((i, j))

            # Add neighbors with next word index
            next_idx = word_idx + 1
            stack.append((i-1, j, next_idx))  # Up
            stack.append((i+1, j, next_idx))  # Down
            stack.append((i, j-1, next_idx))  # Left
            stack.append((i, j+1, next_idx))  # Right

        return False

    # Try starting from each cell
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j):
                return True

    return False

# Test it
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word = "ABCCED"
result = word_search(word, board)
print(result)
