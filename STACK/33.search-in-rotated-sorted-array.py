"""#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
# @lc code=end

"""

arr=[1,2,3,4,3,5,6,7]
left,right=0,len(arr)-1
def find_pivot(arr:list,left,right):
    while left<=right:
        mid=(left+right)//2
        if arr[mid]>arr[mid+1]:
            return mid+1
        else:
            arr[left]>arr[mid]
            #then the middle element
            #inside
        