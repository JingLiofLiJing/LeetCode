class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        std::vector<int32_t> res;
	    std::size_t align = 0ul;
	    if (!nums.empty()) {
	    	std::unordered_map<int32_t, std::vector<int32_t>> temp;
	    	std::size_t num_vecs = nums.size();
	    	for (std::size_t i = num_vecs; i > 0ul; --i) {
	    		std::size_t row = i - 1;
		    	std::size_t sz = nums[row].size() - 1;
	    		for (std::size_t col = 0ul; col <= sz; ++col) {
	    			temp[row + col].emplace_back(nums[row][col]);
	    		}
	    		align = std::max(align, row + sz);
	    	}
	    	for (std::size_t i = 0ul; i <= align && temp.find(i) != temp.end(); ++i) {
	    		const auto& it = temp[i];
	    		std::copy(it.begin(), it.end(), std::back_insert_iterator<decltype(res)>(res));
	    	}
    	}
    	return res;
    }
};
