#include <set>
#include <assert.h>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        bool flag = false;
        std::set<int> ctrs;
        for(const int& num : nums) {
            if (ctrs.find(num) != ctrs.end()) {
                flag = true;
                break;
            } else {
                const auto& res = ctrs.emplace(num);
                assert(res.second);
            }
        }
        return flag;
    }
};
