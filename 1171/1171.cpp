#include <unordered_map>
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
	// 第一次记录每个节点累积的值即可[key 值， value 位置]，相等的话保持最后一个位置
	// 第二次如果i位置的和不是最后一次该和的位置，中间的全部消掉，直接移动next到最后一次的位置的next
	// 然后继续走即可，因为中间满足了可以直接去掉
    ListNode* removeZeroSumSublists(ListNode* head) {
        std::unordered_map<int, ListNode*> ptr_map;
        ListNode prev(0), *h = &prev;
        prev.next = head;
        int msum = 0;
        while(h) {
            msum += h -> val;
            ptr_map[msum] = h;
            h = h -> next;
        }
        h = &prev;
        msum = 0;
        while (h) {
            msum += h -> val;
            h -> next = ptr_map[msum] -> next;
            h = h -> next;
        }
        return prev.next;
    }
};
