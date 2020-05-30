/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <stack>
#include <utility>
 
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> res;
        if (root) {
            // 栈中如果top出现了NULL，则从某一中点开始所有右边的都已经遍历完，需要while
            // 一直删除这一条右链，然后定位上面的中点，然后继续放置右链，重复即可
            // 栈顶出现NULL只可能是右节点的NULL。
            std::stack<TreeNode*> hxd;
            hxd.push(root);
            while(!hxd.empty()) {
                auto node = hxd.top();
                if (!node) {
                    hxd.pop();
                    while ((!hxd.empty()) && ((hxd.top()) -> right == node)) {
                        node = hxd.top();
                        hxd.pop();
                    }
                    if (hxd.empty()) {
                        break;
                    } else {
                        res.push_back(hxd.top() -> val);
                        hxd.push(hxd.top() -> right);
                    }
                }
                else if (node -> left) {
                    hxd.push(node -> left);
                } else {
                    res.push_back(node -> val);
                    hxd.push(node -> right);
                }
            }
        }
        return std::move(res); 
    }
};
