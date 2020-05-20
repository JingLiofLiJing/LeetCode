class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int bts[32]{};
        int base;
        // 补码表示, 值范围是[1, 8), 即四位的有符号整数 0001 - 0111
        // 所以对于num的算术右移会有成为0的情况。
        for (int& num : nums){
            base = 0;
            while((base < 32) && num ){
                if (num & 1) {
                    bts[base] = (bts[base] + 1) % 3;
                }
                base += 1;
                num = num >> 1; 
            }
        }
        int res = 0;
        for (int i = 0; i < 32; ++i) {
            if (bts[i]) {
                res += (1 << i);
            }
        }
        return res;
    }
};
