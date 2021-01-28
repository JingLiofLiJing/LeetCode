class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        std::size_t sz = arr.size();
	    std::size_t num = sz >> 2;
	    sz -= num;
		// 如果小于4的size，第一个肯定是答案
        int32_t val = arr[0];
	    for (std::size_t i = 0ul; i < sz; ++i) {
		    val = arr[i];
		    if (val == arr[i + num]) {
			    break;
		    }
	    }
        return val;
    }
};
