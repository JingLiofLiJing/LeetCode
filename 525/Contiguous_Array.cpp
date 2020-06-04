#include <unordered_map>
#include <algorithm>
#include <stdint.h>
#include <cassert>

class Solution {
    // value in [0, 49999], so int is ok.
    using map = std::unordered_map<int32_t, int32_t>;
public:
    // [0, i] 和 [0, j] 的和都为k，则 [i+1, j]的和为0
    // 对于同值的多个位点，只需要保存最左边的即可，当前的减去最左边的就是当前最大的
    int findMaxLength(vector<int>& nums) {
        map dt{{0, -1}};
        int32_t res = 0, calsum = 0;
        int32_t sz = nums.size();
        assert(sz >= 0);
        for (int32_t i = 0; i < sz; ++i) {
            calsum += (nums[i] == 0 ? -1 : 1);
            if (dt.find(calsum) != dt.end()) {
                res = std::max(res, i - dt[calsum]);
            } else {
                dt[calsum] = i;
            }
        }
        return res;
    }
};
