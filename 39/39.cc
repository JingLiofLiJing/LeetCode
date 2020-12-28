class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        std::unordered_map<int32_t, std::vector<std::vector<int32_t>>> dp;
		for (int32_t i = 0; i < target; ++i) {
			dp[i] = std::vector<std::vector<int32_t>>();
		}
		// 依次考虑全部放某一个即可
		// 不可直接传统做法，会产生全排列的无序情况
		// 背包问题的解法是单一不重复的，否则用动态规划传统得到所有有顺序的解
		for (int32_t val : candidates) {
			dp[val].emplace_back(std::vector<int32_t >{val});
			for (int32_t j = val + 1; j <= target; ++j) {
				auto& content = dp[j];
				const std::vector<std::vector<int32_t>>& infer_val = dp[j - val];
				for (std::vector<int32_t> v : infer_val) {
					v.push_back(val);
					content.emplace_back(std::move(v));
				}
			}
		}
		return dp[target];
    }
};
