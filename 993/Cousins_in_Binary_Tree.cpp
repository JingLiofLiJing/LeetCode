#include <queue>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isCousins(TreeNode* root, int x, int y) {
        std::queue<TreeNode*> before, now;
        bool flagx = false, flagy = false;
        bool tempx = false, tempy = false;
        if (root) {
            now.push(root);
            while (!now.empty()) {
                flagx = false;
                flagy = false;
                while (!now.empty()) {
                    auto ptr = now.front();
                    now.pop();
                    tempx = false;
                    tempy = false;
                    if (ptr -> left) {
                        auto lv = ptr -> left -> val;
                        if (lv == x) {
                            tempx = true;
                            flagx = true;
                        } else if (lv == y) {
                            tempy = true;
                            flagy = true;
                        }
                        before.push(ptr -> left);
                    }
                    if (ptr -> right) {
                        auto rv = ptr -> right -> val;
                        if (rv == x) {
                            if (tempy) {
                                return false;
                            }
                            flagx = true;
                        } else if (rv == y) {
                            if (tempx) {
                                return false;
                            }
                            flagy = true;
                        }
                        before.push(ptr -> right);
                    }
                    if (flagx and flagy) {
                        return true;
                    }
                }
                now.swap(before);
            }
        }
        return false;
    }
};
