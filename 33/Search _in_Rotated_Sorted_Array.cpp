class Solution {
public:
	int search(vector<int>& nums, int target) {
		int32_t beg = 0, end = nums.size() - 1, mid = 0;
		int32_t res = -1;
		while (beg <= end) {
			mid = (beg + end) >> 1;
			if (nums[mid] == target) {
				res = mid;
				break;
			}
			// 一路递增，值区间（nums[mid], nums[end]]
			if (nums[end] > nums[mid]) {
				if (target > nums[mid] && target <= nums[end]) {
					beg = mid + 1;
				}
				else {
					end = mid - 1;
				}
			} 
			// 中间折断了，值区间 (nums[mid], ...] 或者 [..., nums[end]]
			else{
				if (target > nums[mid] || target <= nums[end]) {
					beg = mid + 1;
				}
				else {
					end = mid - 1;
				}
			}
		}
		return res;
	}
};
