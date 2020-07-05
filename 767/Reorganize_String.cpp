#include <unordered_map>
#include <algorithm>
#include <iostream>
class Solution {
public:
    string reorganizeString(string S) {
        size_t sz = S.size();
        std::string res;
        res.resize(sz);
		
		// 记录每个字符出现的次数，然后按照次数降序排序
        std::vector<std::pair<char, size_t>> cal(26, {'a', 0ul});
        for(int i = 0; i < 26; ++i) {
            cal[i].first += i;
        }
        for(char i : S) {
            cal[i - 'a'].second++;
        }
        std::sort(cal.begin(), cal.end(), [](
            const std::pair<char, int32_t>& a,
            const std::pair<char, int32_t>& b){
                return a.second > b.second;
            });
			
		// 当出现最多的字符出现了多于(sz + 1)/ 2次后，剩下的其他字符不能填满中间的空隙，所以才会失败
		// 否则只要不多于阈值，则剩下的洞可以由其他的填满，剩下的一定不会冲突。
        if (cal[0].second > (sz + 1)/ 2) {
            return "";
        }
		// 轮流构造然后冲就行了
        size_t idx = 0ul, rang = cal[0].second;
        std::vector<std::string> temp(rang, std::string(1ul, cal[0].first));
        for(int i = 1; i < 26; ++i) {
            size_t ts = cal[i].second;
            for (size_t j = 0ul; j < ts; ++j) {
                temp[(idx++)%rang].push_back(cal[i].first);
            }
        }
        auto it = res.begin();
        for(size_t i = 0ul; i < rang; ++i) {
            res.replace(it, it + temp[i].size(), temp[i]);
            it += temp[i].size();
        }
        return res;
    }
};
