#include <iostream>
#include <stdint.h>
#include <vector>

using namespace std;

// 因为数字是严格按照 0 ~ max-1分布的，正确的布置下每个数字应该就在自己数字下标的地方
// 从头开始每一个位置，如果这个数在自己的位置之前，则涉及该数的区间至少应该延伸到该数字的下标处
// 如果这个数在自己的位置之后，则此位置更大的数肯定会出现在前面，区间一定会扩展到这个位置，提前处理了
// 如果正好在自己的位置，则前面的可以滚成有序的，为最小的一个区间，依次统计即可。
int maxChunksToSorted(vector<int>& arr) {
	using tp = decltype(arr.size());
	tp sz = arr.size();
	int32_t result = 0;
	tp bound = 0; // Umin = 0
	for (tp i = 0; i < sz; ++i) {
		int val = arr[i];
		bound = val > bound ? val : bound;
		if (bound == i) {
			result += 1;
		}
	}
	return result;
}

int main() {
	std::vector<int> inp{ 1,0,4,3,2 };
	std::cout << maxChunksToSorted(inp);
	return 0;
}
