#include <vector>

class Solution {
public:
    int waysToChange(int n) {
        if (n <= 0) {
	    	return 0;
    	}
	    std::vector<int> dp(n + 1, 0);
	    int coins[4]{ 1, 5, 10, 25 };
	    dp[0] = 1;
	    int res = 0;
	    // 为了防止顺序不一致造成的重复，强行让每个硬币依次加入
      	// n种硬币的结果在前n-1种硬币的结果下进行扩展，相当于排了序
      	for (const int& coin : coins) {
	    	for (int i = coin; i <= n; ++i) {
	    		dp[i] += dp[i - coin];
          		dp[i] %= 1000000007;
	    	}
    	}
    	res = dp[n];
    	return res;
    }
};
