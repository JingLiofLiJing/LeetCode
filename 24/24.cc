/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode forehead, *p = &forehead;
        forehead.next = head;
        ListNode *a = nullptr, *b = nullptr;
        while (a = p -> next, a && a -> next) {
            b = a -> next;
            a -> next = b -> next;
            b -> next = a;
            p -> next = b;
            p = a;
        }
        return forehead.next;
    }
};
