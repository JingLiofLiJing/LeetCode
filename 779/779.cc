#include <variant>
#include <string>
#include <iostream>
#include <any>
#include <system_error>
using namespace std;
// 对称性往前缩就行了，数学上的推导在实现时还是要运行时才能出结果，所以for循环是必须的
class Solution {
public:
	int kthGrammar(int N, int K) {
		int32_t reverse_zero = 0;    // false
		int32_t n_num = 1 << (N - 1);
		// 第一行是0，和reverse_zero初始值为0对应，只有一个元素不需要翻转，所以判断条件是 N > 1
		while (N > 1) {
			int32_t num_half = n_num / 2;
			if (K > num_half) {
				reverse_zero = 1 - reverse_zero;
				K -= num_half;
			}
			--N;
			n_num = num_half;
		}
		return reverse_zero ? 1 : 0;
	}
};
