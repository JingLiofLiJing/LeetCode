#include <deque>

class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int count = 0;
        int begin = 0;
        int end = 0;
        int sum = 1;
        while(end < nums.size()) {
            sum *= nums[end];
            while (sum >= k && begin <= end) {
                sum /= nums[begin];
                begin++;
            }
            count += end - begin + 1;
            end++;
        }

        return count;
    }
};
