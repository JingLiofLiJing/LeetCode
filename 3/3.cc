#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // 每个字符可行的开始位置，该字符上一个位置的下一个位置，有效的开始位置
	    int32_t next[128]{ 0 };
	    int32_t left = 0, res = 0;
	    for (int32_t i = 0; static_cast<std::size_t>(i) < s.size(); ++i) {
	    	auto& ch = s[i];
	    	if (next[ch] == 0 || next[ch] < left) {
	    		res = std::max(res, i - left + 1);
	    	} else {
	    		left = next[ch];
    		}
	    	next[ch] = i + 1;
    	}
    	return res;
    }
};
