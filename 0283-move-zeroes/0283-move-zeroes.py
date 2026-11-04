class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        n = len(nums)

        for j in range(0,n):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
        

        for k in range(i,n):
            nums[k]=0
            k+=1