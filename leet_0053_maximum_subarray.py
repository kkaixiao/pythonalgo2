class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0

        cur_sum, result = nums[0], nums[0]

        for index in range(1, len(nums)):
            cur_sum = max(nums[index], cur_sum + nums[index])
            result = max(result, cur_sum)

        return result

    def maxSubArray2(self, nums):
        max_sum = nums[0]

        def maxSub(n):
            nonlocal max_sum
            if n == 0:
                return nums[0]
            max_val = max(maxSub(n - 1) + nums[n], nums[n])
            max_sum = max(max_sum, max_val)

            return max_val

        maxSub(len(nums) - 1)
        return max_sum

nums1 = [-2,1,-3,4,-1,2,1,-5,4]

mysol = Solution()
print(mysol.maxSubArray(nums1))