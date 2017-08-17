# -*- coding:utf-8 -*-
'''
No.88
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 初始化下标ij和nums1的解析位置total，total=m表示nums1搞完了直接添加nums2剩余部分
        total = i = 0
        j = 0
        while j < n:
            if total < m and nums1[i] <= nums2[j]:
                i += 1
                total += 1
            elif total == m or nums1[i] > nums2[j]:
                nums1.pop()
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
        #return nums1


print Solution().merge([1],1,[],0)
