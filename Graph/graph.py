class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if arr[j+1]>arr[j]:
                    arr[j+1],arr[j]=arr[j],arr[j+=1]

        return arr