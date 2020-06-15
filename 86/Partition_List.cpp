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
    ListNode* partition(ListNode* head, int x) {
	    ListNode prev(-1);
	    prev.next = head;
    	ListNode* mv = &prev;
	    ListNode* nx = mv;
    	ListNode* temp = nullptr;
    	while (nx -> next) {
	    	temp = nx -> next;
			// 由于 < 的条件满足情况，下一次迭代是nx还是保持不动，nx的next变了，不能跳过
			// 如果 nx 和 mv一样，说明之前都是小于的，则两个都要动，因为不涉及链表的修改
		    if (temp -> val < x) {
			    if (nx != mv) {
			    	nx->next = temp->next;
			    	temp->next = mv->next;
		    		mv->next = temp;
		    	} else {
		    		nx = nx->next;
		    	}
		    	mv = mv->next;
	    	} else {
	    		nx = nx->next;
	    	}
	    }
	    return (prev.next);
    }
};
