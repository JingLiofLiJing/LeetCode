class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int32_t symbol_num = 0;
		// 其他的重复数字在 异或 时已经为 0 消掉, 假设单独数字为 res1 和 res2
		// 则 symbol_num = res1 ^ res2;
        for (auto v : nums) {
            symbol_num ^= v;
        }
		// 最低位为 1 的表示，表示 res1 和 res2 在此位上表示不同
        int32_t sig = (symbol_num & (symbol_num - 1)) ^ symbol_num;
        int32_t res1 = 0, res2 = 0;
		// 在 该表示位上都为 1 的数字异或，筛选出 其中一个单独的数字
        for (auto v : nums) {
            if (v & sig) {
                res1 ^= v;
            }
        }
		// 筛选出另一个单独的数字
        res2 = res1 ^ symbol_num;
        return std::vector<int32_t>{res1, res2};
    }
};
