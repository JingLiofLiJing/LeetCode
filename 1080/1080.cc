/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sufficientSubset(TreeNode* root, int limit) {
        if (!root) {
            return root;
        }
        bool l = false, r = false;
        int32_t v = root ->val;
        int32_t next_v = limit - v;
        if (root -> left) {
            root -> left = sufficientSubset(root -> left, next_v);
            l = true;
        }
        if (root -> right) {
            root -> right = sufficientSubset(root -> right, next_v);
            r = true;
        }
        if (!(root -> left) && !(root -> right) && (l || r  || v < limit)) {
            return nullptr;
        }
        return root;
    }
};
