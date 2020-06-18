#include <queue>
#include <cassert>
#include <limits>
#include <stdint.h>

class Solution {
public:
    int countSubstrings(string s) {
        using stp = std::string::size_type;
        using qtp = std::queue<stp>::size_type;
        stp sz = s.size();
        // 类型转换检查
        assert(sz <= (std::numeric_limits<uint32_t>::max() >> 1));
        // 存取上一个位置为结尾的回文串的最左边的位置，只有大于1的才会放入，至少能往下在扩展1位
        std::queue<stp> qe;
        // 每个元素自己就是一个回文
        int32_t res = static_cast<int32_t>(sz);
        stp loc = 0;
        qtp l = 0;
        // 第一个位置不用算，只有一个，最左边界再往左不可达,无论偶数还是奇数的回文模式都不能往左边扩展
        for (stp i = 1; i < sz; ++i) {
            l = qe.size();
            while (l) {
                loc = qe.front();
                qe.pop();
				// 相对下一次的i来说这里肯定从最多i-2开始，不会和下面冲突
                if (s[loc - 1] == s[i]) {
                    res += 1;
                    if (loc > 1) {
                        qe.push(loc - 1);
                    }
                }
                --l;
            }
			// 考虑从[i-1，i]为中心的偶数回文串，之前的偶数回文串满足条件会传播，这是从当前偶数串开始的新模式
            if (s[i] == s[i - 1]) {
                res += 1;
                if (i > 1) {
                    qe.push(i - 1);
                }
            }
			// 后面的可以以自己为中心，这是新的模式
            qe.push(i);
        }
        return res;
    }
};
