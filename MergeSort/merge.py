# Fixed merge function (from your earlier code with bug fix)
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    # Copy remaining elements
    while i < len(list1):
        combined.append(list1[i])  # Fixed: was list[i]
        i += 1
    
    while j < len(list2):
        combined.append(list2[j])  # Fixed: was list[j]
        j += 1
    
    return combined

# Fixed mergesort function
def mergesort(mylist):
    # Base case: if list has 1 or 0 elements, it's already sorted
    if len(mylist) <= 1:
        return mylist
    
    # Fix: use len(mylist) instead of mylist
    mid_index = len(mylist) // 2
    left = mergesort(mylist[:mid_index])
    right = mergesort(mylist[mid_index:])
    return merge(left, right)

# Test Cases
def test_mergesort():
    print("Testing MergeSort Implementation")
    print("-" * 40)
    
    # Test Case 1: Empty list
    test1 = []
    result1 = mergesort(test1)
    expected1 = []
    print(f"Test 1 - Empty list:")
    print(f"Input: {test1}")
    print(f"Output: {result1}")
    print(f"Expected: {expected1}")
    print(f"Pass: {result1 == expected1}\n")
    
    # Test Case 2: Single element
    test2 = [5]
    result2 = mergesort(test2)
    expected2 = [5]
    print(f"Test 2 - Single element:")
    print(f"Input: {test2}")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    print(f"Pass: {result2 == expected2}\n")
    
    # Test Case 3: Already sorted list
    test3 = [1, 2, 3, 4, 5]
    result3 = mergesort(test3)
    expected3 = [1, 2, 3, 4, 5]
    print(f"Test 3 - Already sorted:")
    print(f"Input: {test3}")
    print(f"Output: {result3}")
    print(f"Expected: {expected3}")
    print(f"Pass: {result3 == expected3}\n")
    
    # Test Case 4: Reverse sorted list
    test4 = [5, 4, 3, 2, 1]
    result4 = mergesort(test4)
    expected4 = [1, 2, 3, 4, 5]
    print(f"Test 4 - Reverse sorted:")
    print(f"Input: {test4}")
    print(f"Output: {result4}")
    print(f"Expected: {expected4}")
    print(f"Pass: {result4 == expected4}\n")
    
    # Test Case 5: Random unsorted list
    test5 = [3, 1, 4, 1, 5, 9, 2, 6]
    result5 = mergesort(test5)
    expected5 = [1, 1, 2, 3, 4, 5, 6, 9]
    print(f"Test 5 - Random unsorted:")
    print(f"Input: {test5}")
    print(f"Output: {result5}")
    print(f"Expected: {expected5}")
    print(f"Pass: {result5 == expected5}\n")
    
    # Test Case 6: List with duplicates
    test6 = [3, 3, 1, 2, 2, 1]
    result6 = mergesort(test6)
    expected6 = [1, 1, 2, 2, 3, 3]
    print(f"Test 6 - With duplicates:")
    print(f"Input: {test6}")
    print(f"Output: {result6}")
    print(f"Expected: {expected6}")
    print(f"Pass: {result6 == expected6}\n")
    
    # Test Case 7: Two elements
    test7 = [2, 1]
    result7 = mergesort(test7)
    expected7 = [1, 2]
    print(f"Test 7 - Two elements:")
    print(f"Input: {test7}")
    print(f"Output: {result7}")
    print(f"Expected: {expected7}")
    print(f"Pass: {result7 == expected7}\n")
    
    # Test Case 8: Negative numbers
    test8 = [-3, -1, -4, -2]
    result8 = mergesort(test8)
    expected8 = [-4, -3, -2, -1]
    print(f"Test 8 - Negative numbers:")
    print(f"Input: {test8}")
    print(f"Output: {result8}")
    print(f"Expected: {expected8}")
    print(f"Pass: {result8 == expected8}\n")
    
    # Test Case 9: Mixed positive and negative
    test9 = [3, -1, 4, -2, 0]
    result9 = mergesort(test9)
    expected9 = [-2, -1, 0, 3, 4]
    print(f"Test 9 - Mixed positive/negative:")
    print(f"Input: {test9}")
    print(f"Output: {result9}")
    print(f"Expected: {expected9}")
    print(f"Pass: {result9 == expected9}\n")

# Run the tests
if __name__ == "__main__":
    test_mergesort()
