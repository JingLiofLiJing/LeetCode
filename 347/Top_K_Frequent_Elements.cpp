#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;
typedef map<int, int> int_map;
typedef pair<int, int> int_pair;
bool tmp(int_pair a, int_pair b) {
	return a.second > b.second;
}

class Solution {
public:
	vector<int> topKFrequent(vector<int>& nums, int k) {
		if (!nums.empty()) {
			for (auto i = nums.begin(); i != nums.end(); ++i) {
				if (mmap.find(*i) == mmap.end()) {
					mmap[*i] = 0;
				}
				mmap[*i] += 1;
			}
			for (auto i = mmap.begin(); i != mmap.end(); ++i) {
				vec.push_back(int_pair(i->first, i->second));
			}
			sort(vec.begin(), vec.end(), tmp);
			for (int i = 0; i < k; ++i) {
				result.push_back(vec[i].first);
			}
		}
		return result;
	}
private:
	int_map mmap;
	vector<int_pair> vec;
	vector<int> result;
};

int main() {
	vector<int> nums{ 1,1,1,2,2,3 };
	Solution a;
	vector<int> res = a.topKFrequent(nums, 1);
	for (auto i = res.begin(); i != res.end(); ++i) {
		cout << *i << endl;
	}
}