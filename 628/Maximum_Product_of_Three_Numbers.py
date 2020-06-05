#include <algorithm>
class Solution {
public:
    // 三正数 或者 两负数1正数
    int maximumProduct(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        auto iter = nums.end();
        return std::max(
            (*(iter - 1)) * (*(iter - 2)) * (*(iter - 3)),
            (*(iter - 1)) * nums[0] * nums[1]
        );
    }
};
