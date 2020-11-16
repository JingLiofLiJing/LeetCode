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


class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        std::vector<int32_t> res;
	    std::size_t num_vecs = nums.size();
	    if (num_vecs) {
	    	std::size_t all_num = 0ul, max_rc = 0ul;
	    	for (std::size_t i = 0ul; i < num_vecs; ++i) {
	    		std::size_t sz = nums[i].size();
		    	all_num += sz;
	    		max_rc = std::max(max_rc, sz);
	    	}
	    	// 确保不是每一行都没有数据，不然才进行真正的处理。
	    	if (max_rc > 0) {
	    		std::vector<std::size_t> next_available(num_vecs, 0ul);
	    		// 下一个有意义的位置，跳过了之前记录的无效的行
	    		for (std::size_t i = 1ul; i < num_vecs; ++i) {
	    			next_available[i] = i - 1;
	    		}
	    		next_available.shrink_to_fit();
	    		max_rc += num_vecs - 1ul;
		    	res.reserve(all_num);

	    		for (std::size_t start = 0ul; start < max_rc; ++start) {
	    			std::size_t row_start = start, row_end = 0ul;
		    		if (start >= num_vecs) {
		    			row_start = num_vecs - 1;
		    			row_end = max_rc - start;
		    			row_end = row_end >= num_vecs ? 0 : num_vecs - row_end;
	    			}
		    		std::size_t be = row_start;
		    		while (row_start > row_end) {
		    			std::size_t col = start - row_start;
		    			if (col < nums[row_start].size()) {
		    				res.push_back(nums[row_start][col]);
	      					be = row_start;
	    				} else {
	    					next_available[be] = next_available[row_start];
	    				}
	    				row_start = next_available[row_start];
	    			}
	    			if (row_start == row_end) {
	    				std::size_t col = start - row_start;
	    				if (col < nums[row_start].size()) {
	    					res.push_back(nums[row_start][col]);
	    				}
	    			}
	    		}
	    	}
        }
        return res;
    }
};
