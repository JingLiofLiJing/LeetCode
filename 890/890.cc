class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
		std::vector<std::string> res;
		for (std::string word : words) {
			if (Parse(word, pattern)) {
				res.emplace_back(std::move(word));
			}
		}
        return res;
	}

	bool Parse(const std::string& word, const std::string& pattern) {
		std::size_t pt_len = pattern.size();
		if (pt_len != word.size()) {
			return false;
		}
		int a[256]{ 0 }, b[256]{ 0 };
		for (std::size_t i = 0ul; i < pt_len; ++i) {
			char word_ch = word[i];
			char pattern_ch = pattern[i];
            int not_zero_index = i + 1;
			// 相等情况：
			//   1. 如果都没有被绑定，则都是-1，此时绑定下标
			//   2. 如果都被绑定了且绑定的下标相等，则匹配上
			// 不等情况
			//   1. 一个被绑定了一个没被绑定
			//   2. 两个都被绑定了，但是不是对应的
			if (a[word_ch] != b[pattern_ch]) {
				return false;
			}
			a[word_ch] = not_zero_index;
			b[pattern_ch] = not_zero_index;
		}
		return true;
	}
};
