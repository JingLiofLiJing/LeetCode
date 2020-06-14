#include <algorithm>

class Solution {
public:
    // 每一天只有三种情况: 买入、卖出、冷冻期
    // 如果最近为买入的状态，则当天可以卖出或者冷冻
    // 如果最近为卖出的状态，则当天可以买入或冷冻
    // 如果最近为冷冻的状态，则可以买入、卖出或者继续冷冻
    int maxProfit(vector<int>& prices) {
        using tp = decltype(prices.size());
        tp sz = prices.size();
        if (sz < 2) { return 0; }
        vector<int> buy(sz, 0);
        vector<int> sell(sz, 0);
        vector<int> cool(sz, 0);
        buy[0] -= prices[0];
        for (tp i = (tp)1; i < sz; ++i) {
            buy[i] = std::max(buy[i - 1], cool[i - 1] - prices[i]);    // 之前的最后一次操作是买，可以cool，是cool的话可以继续买
            sell[i] = std::max(buy[i - 1] + prices[i], sell[i - 1]);   // 之前的最后一次操作是sell，可以cool，是buy的话可以直接卖
            cool[i] = sell[i - 1];  // 什么情况下都可以无条件cool
        }
        return sell[sz - 1];
    }
};
