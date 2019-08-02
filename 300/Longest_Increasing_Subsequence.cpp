#include <iostream>
#include <vector>
#include <algorithm> 
using namespace std;

class Solution {
private:
	vector<int> tmps;
	int l, r, mid;

	void change(int num) {
		l = 0;
		r = tmps.size() - 1;
		while (l < r) {
			mid = (l + r) >> 1;
			if (tmps[mid] >= num) {
				r = mid;
			}
			else {
				l = mid + 1;
			}
		}
		if (r + 1 == tmps.size() and tmps[r] < num) {
			tmps.push_back(num);
		}
		tmps[r] = min(tmps[r], num);

	}

public:
	int lengthOfLIS(vector<int>& nums) {
		if (nums.size() == 0) {
			return 0;
		}
		else {
			tmps.push_back(nums[0]);
			for (int i = 1; i < nums.size(); ++i) {
				change(nums[i]);
			}
			return tmps.size();
		}
	}
};

int main()
{
	Solution s;
	vector<int> data{ 10,9,5,2,3,2,5,3,7,101,11,29,11,46,78,18 };
	cout << s.lengthOfLIS(data) << endl;
}
