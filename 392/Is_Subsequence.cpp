#include "pch.h"
#include <iostream>
#include <string>

using namespace std;

class Solution1 {
private:
	//*l：左节点 *r：右节点
	int sl = 0, sr;
	int tl = 0, tr;
	bool result = true;
public:
	bool isSubsequence(string s, string t) {
		cout.setf(ios_base::boolalpha);
		sr = s.size() - 1;
		tr = t.size() - 1;
		while (sl <= sr) {
			while (tl <= tr && t[tl] != s[sl]) {
				tl += 1;
			}
			if (tl > tr || tl == tr && sl < sr) {
				result = false;
				break;
			}
			tl += 1;
			sl += 1;
			if (sl > sr) {
				break;
			}
			while (tl <= tr && t[tr] != s[sr]) {
				tr -= 1;
			}
			if (tl > tr || tl == tr && sl < sr) {
				result = false;
				break;
			}
			tr -= 1;
			sr -= 1;
		}
		return result;
	}
};

class Solution2 {
public:
	bool isSubsequence(string s, string t) {
		if (s.empty()) return true;
		int index = 0, len = s.length(), length = t.length();
		for (int i = 0; i < length; ++i) {
			if (t[i] == s[index]) {
				if (index == len - 1) return true;
				++index;
			}
		}
		return false;
	}
};

int main()
{
	Solution s;
	string a{ "a" }, b{ "a" };
	cout << s.isSubsequence(a, b) << endl;
}
