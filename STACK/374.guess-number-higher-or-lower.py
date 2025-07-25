#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left,right=1,n
        while left<=right:
            mid=(left+right)//2
            res=guess(mid)
            
            if res==0:
                return mid
            
            elif res<0:
                right=mid-1
            else:
                left=mid+1
        return -1
                
                
            
        
# @lc code=end

