class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        std::size_t sz = s.size();
        std::vector<std::size_t> dp(sz + 1ul, 0ul);
        dp[0] = 1;
		// 动态规划，dp[i]代表s的从0开始的长度为i的子串是否能够被wordDict组合出来
		// 在计算dp[i]的时候，dp[<i]的都已经被计算出来了，所以可以直接用。
        for(std::size_t len = 1ul; len <= sz; ++len){
            for(const auto& str : wordDict){
                std::size_t strsz = str.size();
				std::size_t dp_from = len - strsz;
                if( strsz <= len && s.substr(dp_from, strsz) == str && dp[dp_from]) {
                    dp[len]=true;
                    break;
                }
            }
        }
        return dp[sz];
    }
}; 
