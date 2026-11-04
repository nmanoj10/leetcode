class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        n = len(nums)

        for j in range(0,n):
            if nums[j]!=0:
                i+=1
                nums[i]=nums[j]
                
        

        for k in range(i+1,n):
            nums[k]=0
            k+=1

        return nums