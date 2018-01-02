# -*- coding: utf-8 -*- 
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution(object):
    def search(self,nums):
        if len(nums) == 1:
            yield [nums[0]]
        for i in xrange(len(nums)):
            if i>0 and nums[i]==nums[i-1] :
                continue
            left = nums[:i] + nums[i+1:]
            for res in self.search(left):
                yield [nums[i]]+res
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        辣鸡方法，相对于不重复的方法检测重复元素，如果重复往后移动即可
        """
        nums.sort()
        res = []
        for i in self.search(nums):
            res.append(i)
        return res

    #java方法，防止重复使用次数used判断，其实和上面方法差不多
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), nums, new boolean[nums.length]);
        return list;
    }

    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, boolean [] used){
        if(tempList.size() == nums.length){
            list.add(new ArrayList<>(tempList));
        } else{
            for(int i = 0; i < nums.length; i++){
                if(used[i] || i > 0 && nums[i] == nums[i-1] && !used[i - 1]) continue;
                used[i] = true; 
                tempList.add(nums[i]);
                backtrack(list, tempList, nums, used);
                used[i] = false; 
                tempList.remove(tempList.size() - 1);
            }
        }
    }
