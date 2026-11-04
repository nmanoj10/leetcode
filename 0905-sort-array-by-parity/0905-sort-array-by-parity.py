class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i = -1
        n = len(nums)
        for j in range(n):
            if nums[j]%2==0:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
        return nums
