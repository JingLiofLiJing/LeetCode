# -*- coding: utf-8 -*- 
'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
'''
def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        长度小于3的肯定符合条件，如果大于3，则设置可使用重定义数为1，然后判断当前的数字
        1.第0位置数字大了，则消耗重定义数，数字重定义为第1为数的值
        2.对于1位置的数字，在之前的0位置数的判断和调整中肯定符合条件，可以不用判断
        3.对于后面i位置的数字（i>=2），如果小于的话，判断和i-2的数字的大小，大的话变更i-1，小的话变更自己，尽量不扰乱下一次比较
        如果在调整完后发现重定义数小于0，则不符合条件
        """
        if len(nums) < 3:
            return True
        use = 1
        for i in range(len(nums)):
            if i == 0 and nums[i] > nums[i+1]:
                nums[i] = nums[i+1]
                use -= 1
            elif i > 1 and nums[i] < nums[i-1]:
                if nums[i] >= nums[i-2]:
                    use -= 1
                    nums[i-1] = nums[i]
                elif nums[i] < nums[i-2]:
                    use -= 1
                    nums[i] = nums[i-1]
            if use < 0:
                return False
        return True
