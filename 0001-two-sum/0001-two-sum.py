class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_idx = {} 
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in num_to_idx:
                return [num_to_idx[compliment],i]
            num_to_idx[num] = i
        return []
            