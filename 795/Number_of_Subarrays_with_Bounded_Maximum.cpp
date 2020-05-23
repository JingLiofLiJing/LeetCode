#include <stdint.h>
#include <algorithm>

class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& A, int L, int R) {
        int32_t res = 0, count = 0;
        // dp 的长度多1是为了方便解决第一个元素，不然for循环里面得加入if
        // dp[i]的值代表以i为最后一个元素的满足要求的序列的个数
        // 如果i小于L，则只能通过i-1的个数直接添加在后面得到，所以此时dp[i] = dp[i-1]，但是此时可能会成为后面某个在区间内的k位置的满足条件的
        // 序列内容之一，比如[1,2,3,1,1,2,3]，假设L为2，R为3; 第二个1和第三个1会成为新的满足条件的序列的一部分，即中间的[1,1,2,3]，所以count
        // 记录这样新开始的小于L的元素个数
        // 如果i在区间内，则当前满足条件的个数不仅包含i-1的个数，同时会加上之前聚集的小于L的值的个数，由count来描述
        // 如果i大于R，则之前聚集的小于L的值序列不能满足要求，同时当i在区间内的时候已经计算了前面聚集的小于L的数值的情况，所以这两种情况下count需要
        // 置位为0.
        vector<int> tmp(A.size() + 1, 0);
        using tp = decltype(A.size());
        tp sz = A.size();
        for(tp i = 0; i < sz; ++i) {
            int num = A[i];
            if (num <= R) {
                count += 1;
                tmp[i + 1] = tmp[i] + (num < L ? 0 : count);
                res += tmp[i + 1];
            }
            if (num >= L) {
                count = 0;
            }
        }
        return res;
    }
};
