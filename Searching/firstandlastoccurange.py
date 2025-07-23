# Runtime Complexity: O(n) in worst case
# - The initial binary search is O(log n)
# - However, the while loops to find leftmost and rightmost positions can take O(n) time
#   in the worst case when all elements in the array are the same as the target
# - Therefore, overall time complexity is O(n)
# Space Complexity: O(1) - only using a constant amount of extra space
def find(arr:list,target:int):
    if not arr:
        return (0, 0)

    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            leftmost = mid
            while leftmost > 0 and arr[leftmost - 1] == target:
                leftmost -= 1
                break


            rightmost = mid
            while rightmost < len(arr) - 1 and arr[rightmost + 1] == target:
                rightmost += 1
                break

            return leftmost
        if arr[mid]<target:
            left=mid+1
        else:
            right=mid-1


    return [-1,-1]





# Sample inputs for testing
if __name__ == "__main__":
    # Test case 1: Target found in array
    print(find([1, 2, 3, 4, 5], 3))  # Expected: 2

    # Test case 2: Target not in array, between elements
    print(find([1, 2, 4, 5, 6], 3))  # Expected: (1, 2)

    # Test case 3: Target smaller than all elements
    print(find([2, 3, 4, 5, 6], 1))  # Expected: (0, 0)

    # Test case 4: Target larger than all elements
    print(find([1, 2, 3, 4, 5], 6))  # Expected: (4, 4)

    # Test case 5: Empty array
    print(find([], 1))  # Expected: (0, 0)

    # Test case 6: Single element array, target found
    print(find([5], 5))  # Expected: 0

    # Test case 7: Single element array, target not found
    print(find([5], 3))  # Expected: (0, 0)

    # Test case 8: Array with duplicates
    print(find([1, 2, 2, 2, 5], 2))  # Expected: 1, 2, or 3
