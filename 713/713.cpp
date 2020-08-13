#include <deque>

#不会溢出的版本，需要用空间换取
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int32_t res = 0;
		std::deque<int> temp;
		for (const auto& num : nums) {
			if (num >= k) {
				temp.clear();
			}
            else if (num == 1) {
				res += temp.size() + 1;
				temp.push_back(num);
			}
			else {
				while (temp.size() && temp.front() * num >= k){
					temp.pop_front();
				}
				for (auto it = temp.begin(); it!= temp.end(); ++it) {
					*it *= num;
				}
				res += temp.size() + 1;
				temp.push_back(num);
			}
		}
		return res;
    }
};
