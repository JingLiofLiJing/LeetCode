/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        int cnt = 0;
        ListNode* p = root;
        // 计算节点的个数做分配
        while (p) {
            cnt++;
            p = p->next;
        }
        // 每个节点都有base个，多出来的md个分配给前md个节点
        int base = cnt/k, md = cnt%k;
        vector<ListNode*> res(k, nullptr);
        ListNode* cur = root,* pre = nullptr;
        for (int i = 0; i < k; i++) {
            int ln = base + (i < md ? 1 : 0);
            if (ln == 0) {continue;}
            res[i] = cur;
            while (ln--) {
                pre = cur;
                cur = cur->next;
            }
            pre -> next = nullptr;
        }
        return res;
    }
};
