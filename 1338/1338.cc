// 最常规的解法而已，先记录次数然后降序排序再统计即可
class Solution {
public:
    int minSetSize(vector<int>& arr) {
        std::unordered_map<int32_t, std::size_t> umap;
        int32_t ans = 0;
        std::size_t arr_sz = arr.size();
        for(int32_t val : arr) {
            auto res = umap.emplace(val, 0ul);
            ++(res.first -> second);
        }
        std::vector<std::size_t> temp;
        for(const auto& it : umap){
            temp.push_back(it.second);
        }
        std::sort(temp.begin(),temp.end(), [](std::size_t a, std::size_t b) {
            return a > b;   
        });
        std::size_t sz = temp.size();
        std::size_t cnt = 0ul;
        for(std::size_t i = 0ul; i < sz; ++i) {
            cnt += temp[i];
            ++ans;
            if (cnt * 2ul >= arr_sz) {
                break;
            }
        }
        return ans;
    }
};
