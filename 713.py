'''
Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.
'''
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        连续子序列的乘积小于k，则r表示以当前位置为结尾的连续串，l表示串的左边界，l-r+1表示以r为结尾符合要求的子串数量，
        所以遍历r即可，每次在新r内更新l找到符合要求的最左边界统计即可
        """
        if nums == [] or k <= 1:
            return 0
        res = l = r = 0
        prod = 1
        while r < len(nums):
            prod *= nums[r]
            while prod >= k:
                prod /= nums[l]
                l += 1
            res += r - l + 1
            r += 1
        return res
