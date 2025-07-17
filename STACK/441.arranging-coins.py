#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            
            coins = (mid * (mid + 1)) // 2
            
            if coins <= n:  
                res = mid   
                left = mid + 1
            else:         
                right = mid - 1
                
        return res
        
        
# @lc code=end

