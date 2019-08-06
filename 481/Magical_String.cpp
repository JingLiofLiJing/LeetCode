#include "pch.h"
#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;

class Solution {
private:
	int num, index, result;
	vector<int > v{ 1,2,2 };
public:
	int magicalString(int n) {
		if (n == 0) {
			return 0;
		}
		else if (n < 4) {
			return 1;
		}
		result = 1;
		num = 1;
		index = 2;
		while (v.size() < n) {
			for (int i = 0; i < v[index]; ++i) {
				v.push_back(num);
				if (num == 1) {
					result += 1;
				}
				if (v.size() == n) {
					return result;
				}
			}
			index += 1;
			num = 2 / num;
		}
	}
};

int main()
{
	Solution s;
	int limit = 555;
	cout << s.magicalString(limit) << endl;
}
