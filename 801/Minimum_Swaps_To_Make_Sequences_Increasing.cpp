#include <stdint.h>
#include <tuple>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int minSwap(vector<int>& A, vector<int>& B) {
	vector<int>::size_type size = A.size();
	// 对于每一步的状态，在第i步时最后的状态可能是i位置的AB元素不交换或者交换，这都会影响到未来的最优选择，所以必须都保存
	vector<vector<int32_t>> dp(2, vector<int32_t>(size, static_cast<int32_t>(size)));
	// 第1个vector代表i位置时结果为不修改位置时的最小情况，第二个为交换了位置的情况
	// 递推情况显然满足动态规划的假设
	dp[0][0] = 0;
	dp[1][0] = 1;
	for (vector<int>::size_type i = 1ul; i < size; ++i) {
		// 不交换位置下的判断
		if (A[i] > A[i - 1] && B[i] > B[i - 1]) {
			dp[0][i] = std::min(dp[0][i], dp[0][i - 1]);
			dp[1][i] = std::min(dp[1][i], dp[1][i - 1]) + 1; // 第i个位置交换时已经多了一次交换的次数
		}
		// 交换位置下的判断，这里不能else，因为会存在 两个 i - 1 都小于 i的情况，需要根绝前一次的结果来进行具体计算
		if (A[i] > B[i - 1] && B[i] > A[i - 1]) {
			dp[0][i] = std::min(dp[0][i], dp[1][i - 1]);
			dp[1][i] = std::min(dp[1][i], dp[0][i - 1]) + 1;
		}
	}
	return std::min(dp[0][size - 1], dp[1][size - 1]);
}


int main() {
	std::vector<int> a{0,4,4,5,9};
	std::vector<int> b{0,1,6,8,10};
 	std::cout << minSwap(a,b) << std::endl;
	return 0;
}
