class Solution {
public:
   // 前置条件，A或者B内相邻的区间不会有重叠，包括两端，否则应该合成一个区间
   // 所以用两个下标分别记录A和B的遍历进度，处理完当前 i 和 j 的包含关系后
   // 如果A的结尾更后面，则B的下标+1，反之A的下标+1
   // 因为区间不会相邻，所以当当前A和B的后端一样时，会在两步后同时移动后一位，即 i+1 和 j+1
    vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        using tp = typename vector<vector<int>>::size_type;
		vector<vector<int>> result;
		tp sz1 = A.size(), sz2 = B.size();
		tp i = (tp)0, j = (tp)0;
		vector<int> tempA, tempB;
		int l, r;
		while (i < sz1 and j < sz2) {
			tempA = A[i];
			tempB = B[j];
			l = std::max(tempA[0], tempB[0]);
			r = std::min(tempA[1], tempB[1]);
			if (l <= r) {
				result.emplace_back(std::initializer_list<int>{ l, r });
			}
			if (r == tempA[1]) {
				i += 1;
			} else {
				j += 1;
			}
		}
		return result;
    }
};
