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
    bool check(TreeNode* left, TreeNode* right) {
        if (left && right) {
            return (left -> val == right -> val)
                   && check(left -> left, right -> right)
                   && check(left -> right, right -> left);
        }
        return (!left && !right) ? true : false;
    }
    
    bool isSymmetric(TreeNode* root) {
        return root ? check(root -> left, root -> right) : true;
    }
};
