class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows = len(board)
        cols = len(board[0])

        def dfs(start_i, start_j):
            stack = [(start_i, start_j, 0, set())]  # (row, col, word_index, visited_path)

            while stack:
                i, j, word_idx, visited = stack.pop()

                # Check bounds
                if i < 0 or i >= rows or j < 0 or j >= cols:
                    continue

                # Check if already visited in this path or character doesn't match
                if (i, j) in visited or board[i][j] != word[word_idx]:
                    continue

                # If we found the whole word
                if word_idx == len(word) - 1:
                    return True

                # Create new visited set for this path
                new_visited = visited.copy()
                new_visited.add((i, j))

                # Add neighbors with next word index
                next_idx = word_idx + 1
                stack.append((i-1, j, next_idx, new_visited))  # Up
                stack.append((i+1, j, next_idx, new_visited))  # Down
                stack.append((i, j-1, next_idx, new_visited))  # Left
                stack.append((i, j+1, next_idx, new_visited))  # Right

            return False

        # Try starting from each cell
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j):
                    return True

        return False
