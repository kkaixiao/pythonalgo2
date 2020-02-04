class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0

        cur_sum, result = nums[0], nums[0]

        for index in range(1, len(nums)):
            cur_sum = max(nums[index], cur_sum + nums[index])
            result = max(result, cur_sum)

        return result

nums1 = [-2,1,-3,4,-1,2,1,-5,4]

mysol = Solution()
print(mysol.maxSubArray(nums1))