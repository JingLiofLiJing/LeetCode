/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
#include <stack>

class Solution {
public:
    vector<int> preorder(Node* root) {
        std::vector<int> res;
        if (root) {
            std::stack<Node*> tasks;
            tasks.push(root);
            while (!tasks.empty()) {
                Node* now = tasks.top();
                tasks.pop();
                res.push_back(now -> val);
                auto childs = now -> children;
                if (!childs.empty()) {
                    for (auto target = childs.rbegin();
                        target != childs.rend();
                        ++target) {
                        tasks.push(*target);
                    }
                }
            }
        }
        return res;
    }
};
