class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        std::size_t hw = img1.size();
		int32_t overlap = 0;
		for (std::size_t i = 1ul; i <= hw; ++i) {
			for (std::size_t j = 1ul; j <= hw; ++j) {
				int32_t lt = 0, br = 0, lb = 0, rt = 0;
				// 1. A: [hw - i, hw) -> [hw - j, hw)
				//    B: [0, i] -> [0, j]
				// 2. A: [0, i] -> [0, j]
				//    B: [hw - i, hw) -> [hw - j, hw)
				for (std::size_t m = 0ul; m < i; ++m) {
					for (std::size_t n = 0ul; n < j; ++n) {
						std::size_t p = hw - i + m;
						std::size_t q = hw - j + n;
						lt += (img1[p][q] && img2[m][n] ? 1 : 0);
						br += (img1[m][n] && img2[p][q] ? 1 : 0);
						lb += (img1[m][q] && img2[p][n] ? 1 : 0);
						rt += (img1[p][n] && img2[m][q] ? 1 : 0);
					}
				}
				overlap = std::max({ overlap, lt, br, lb, rt });
			}
		}
		return overlap;
    }
};

// 位移的方法就完事了
class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        std::size_t hw = img1.size();
		int32_t overlap = 0;

		std::vector<int32_t> lines1(hw, 0), lines2(hw, 0);
		for (std::size_t i = 0ul; i < hw; ++i) {
			auto& num1 = lines1[i];
			auto& num2 = lines2[i];
			for (std::size_t j = 0ul; j < hw; ++j) {
				num1 <<= 1;
				num1 += img1[i][j];
				num2 <<= 1;
				num2 += img2[i][j];
			}
		}
		decltype(lines1) temp1 = lines1;
		decltype(lines2) temp2 = lines2;
		for (std::size_t i = 0ul; i < hw; ++i) {
			for (std::size_t j = 0ul; j < hw; ++j) {
				int tmpsuma_t = 0, tmpsuma_b = 0;
				int tmpsumb_t = 0, tmpsumb_b = 0;
				for (std::size_t k = 0ul; k < hw - j; ++k) {
					std::size_t t1 = k, t2 = k + j;
					// img1右移 并在 img2 的下方
					int32_t ta = temp1[t1] & lines2[t2];
					// img1左移 并在 img2 的下方
					int32_t tb = temp2[t1] & lines1[t2];
					while (ta) {
						++tmpsuma_t;
						ta &= (ta - 1);
					}
					while (tb) {
						++tmpsumb_t;
						tb &= (tb - 1);
					}

					// img1右移 并在 img2 的上方
					ta = temp1[t2] & lines2[t1];
					// img1左移 并在 img2 的上方
					tb = temp2[t2] & lines1[t1];
					while (ta) {
						++tmpsuma_b;
						ta &= (ta - 1);
					}
					while (tb) {
						++tmpsumb_b;
						tb &= (tb - 1);
					}

					overlap = std::max({ overlap , tmpsuma_b , tmpsumb_b, tmpsuma_t, tmpsumb_t });
				}
			}
			for (std::size_t j = 0ul; j < hw; ++j) {
				temp1[j] >>= 1;
				temp2[j] >>= 1;
			}
		}
		return overlap;
    }
};

