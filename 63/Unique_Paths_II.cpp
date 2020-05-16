class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid.empty() || obstacleGrid[0].empty() || obstacleGrid[0][0]) {
            return 0;
        }
        decltype(obstacleGrid.size()) m = obstacleGrid.size();
        decltype(m) n = obstacleGrid[0].size();
        // 额外在上面和左边增加一行和一列，方便统一的循环逻辑，循环的轮数不变，额外多两个int的空间，可接受
        std::vector<int> before(n + 1, 0), after(n + 1, 0);
        // 痛过排除，入口元素肯定是1，所以借助第一次的before[1] 来强制让初始的步数为1
        before[1] = 1;
        for (decltype(m) i = 0; i < m; ++i) {
            for(decltype(n) j = 0; j < n; ++j) {
                after[j + 1] = obstacleGrid[i][j] ? 0 : after[j] + before[j + 1];
            }
            before.swap(after);
        }
        return before[n];
    }
};
