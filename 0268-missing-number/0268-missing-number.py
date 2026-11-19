class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        m = n*(n+1)/2
        ans = 0
        for num in nums:
            ans+=num
        return int(m-ans)