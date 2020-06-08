#include <stdint.h>
#include <algorithm>

class Solution {
public:
    int numberOfSubstrings(string s) {
		using tp = decltype(s.size());
		tp sz = s.size();
		if (sz < 3) {
		    return 0;
		}
		// 每个字符最后一次出现的下标位置，不包括目前i位置的字符，先计算再更新位置。
		int32_t a[3]{ -1,-1,-1 };
		int32_t res = 0, i = 0;
		// 分别表示最近出现的最远的位置的字符是哪一个
		int32_t first = -1, second = -1, third = -1;
		int32_t temp = 0, index;
		while (i < sz) {
		    // 计算字符所对应的的偏移
		    index = s[i] - 'a';
		    // 首次添加，就是第一远
		    if (first == -1) {
			    first = index;
		    }
		    // 由于后面while循环，所以这里的字符肯定和first出现的字符不一样
		    else if (second == -1) {
			    second = index;
		    }
			else if (third == -1) {
				// 第一种：最远的最近出现字符又出现了，没有凑够三个字符，所以temp为0，但是更新出现次序
				// 原first出现的字符在这次之后比原second出现的字符更近了，交换first和second的顺序
				if (index == first) {
					std::swap(first, second);
				}
				// 否则首次凑够全部字符了，此时前面满足条件的为first的字符位置+1，比如aabc
				// aabc  abc 
				else {
					temp = a[first] + 1;
					third = index;
				}
			}
			// 如果三种字符都出现过后，那个这个字符不是first字符就是second字符
			else if (first == index) {
				// aabbcca  ->  aabbcca  abbcca bbcca
				temp = a[second] + 1;
				std::swap(first, second);
				std::swap(second, third);
			}
			// 否则second字符，不增加新的结果类型，只能在原来的尾部添加该字母得到平凡的结果，temp不用修改。
			else {
				std::swap(second, third);
			}
			res += temp;
			++i;
			while (i < sz && s[i] == s[i - 1]) {
				res += temp;
				++i;
			}
			// 记录最后一次出现的位置
			a[index] = i - 1;
		}
		return res;
	}
};
