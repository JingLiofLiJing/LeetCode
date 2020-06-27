#include <iostream>
#include <cmath>

class Solution {
public:
    // 一部分是0 - 999..99 的整体的0的个数，当为n位时，这个值可以为[n-1]位的值*10 + 10^(n-1)
	// 比如说 0 - 25是9，则计算425时，首先记录了base为9，然后0-99为20，第三位如果小于2,
	// 相当于高位加入不会添加额外的2，如果正好为2，不等于2的高位可以直接乘上原来的base，当高位是2时
	// 由于不能累计到299，所以相当于200-225，多了25+1=26个高位的2，然后低位的25用原来的res就行。
	// 如果高位大于2，则res等于0-99的满0-399，然后在加上res即可。
    // 一部分是不满时的到限制的个数
    int numberOf2sInRange(int n) {
        // base 代表迭代到n位时， [0, 10^(n) - 1)] 一共有的2的个数
        // 其值为 n-1 位的值乘10（即高一位为0-9）再加上 10^（n-1）次方，因为2开头的数字一共有10^（n-1）
        int32_t base = 0;
        int32_t mt = 0;
        // 从低位到高位迭代到第n位时的结果，后面的相当于在前面拼了0-9
        int32_t res = 0;
        int32_t cost = 0;
        int32_t md = 0;
        while(n) {
            md = n % 10;
            if (md < 2) {
                res = md * base + res;
            } else if (md == 2) {
                res = md * base + res + cost + 1;
            } else if (md > 2) {
                res = md * base + res + std::pow(10, mt);
            }
            n = n / 10;
            if (n) {
                base = base * 10 + std::pow(10, mt);
                cost = md * std::pow(10, mt) + cost;
                mt += 1;
            }
        }
        return res;
    }
};
