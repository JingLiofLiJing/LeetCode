class Solution {
public:
    /*
     *  如果左边的大，则在左边找，右边大则右边找
     *  否则当前即为peak，直到空间左右压缩到一起即可
     */
    int findPeakElement(vector<int>& nums) {
        std::size_t sz = nums.size();
        std::size_t start = 0ul, end = sz - 1;
        while (start < end) {
            auto mid = (start + end) >> 1;
            if (mid > start && nums[mid - 1] >= nums[mid]) {
                end = mid - 1;
            } else if ((mid < end) && nums[mid + 1] >= nums[mid]) {
                start = mid + 1;
            } else {
                return mid;
            }
        }
        return start;
    }
};
