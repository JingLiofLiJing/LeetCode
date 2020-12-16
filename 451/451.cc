class Solution {
public:
    string frequencySort(string s) {
        int count[256]{ 0 };
		std::size_t sz = s.size();
		for (std::size_t i = 0ul; i < sz; ++i) {
			++count[s[i]];
		}
		std::sort(s.begin(), s.end(), [&count](char a, char b) {
			auto ca = count[a], cb = count[b];
			if (ca == cb) {
				return a > b;
			}
			return count[a] > count[b];
		});
		return s;
    }
};
