class Solution {
public:
    int minFlips(int a, int b, int c) {
        int32_t a_bit = 1, b_bit = 1, c_bit = 1;
		int32_t res = 0;
		for (int32_t i = 0; i < 31; ++i) {
			int32_t at = a & a_bit ? 1 : 0;
			int32_t bt = b & b_bit ? 1 : 0;
			int32_t ct = c & c_bit ? 1 : 0;
			if (ct) {
				res += (1 - (at || bt));
			}
			else {
				res += (at + bt);
			}
			if (i < 31) {
				a_bit <<= 1;
				b_bit <<= 1;
				c_bit <<= 1;
			}
		}
		return res;
    }
};
// 位运算就完事了
