#include <deque>

class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        int32_t res = 0;
        if (root) {
            std::deque<TreeNode*> temps(1, root);
            int32_t len;
            while ((len = temps.size()) > 0) {
                res = 0;
                for (int32_t i = 0; i < len; ++i) {
                    TreeNode* head = temps.front();
                    temps.pop_front();
                    res += head -> val;
                    if (head -> left) {
                        temps.push_back(head -> left);
                    }
                    if (head -> right) {
                        temps.push_back(head -> right);
                    }

                }
            }
        }
        return res;
    }
};
