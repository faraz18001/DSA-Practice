def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    top, bottom = 0, len(matrix) - 1
    
    # First, find the correct row using binary search
    while top <= bottom:
        current_row = (top + bottom) // 2
        
        if target < matrix[current_row][0]:
            # Target is smaller than first element, go to upper rows
            bottom = current_row - 1
        elif target > matrix[current_row][-1]:
            # Target is larger than last element, go to lower rows
            top = current_row + 1
        else:
            # Target is in this row, break and search within the row
            break
    else:
        # No valid row found
        return False
    
    # Now search within the found row
    left, right = 0, len(matrix[0]) - 1
    while left <= right:
        mid_point = (left + right) // 2
        
        if matrix[current_row][mid_point] < target:
            left = mid_point + 1
        elif matrix[current_row][mid_point] > target:
            right = mid_point - 1
        else:
            return True
    
    return False


