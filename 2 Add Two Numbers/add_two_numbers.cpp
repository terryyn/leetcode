
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode begin(0);
        ListNode* iterator = &begin;
        while(l1!=NULL&&l2!=NULL)
        {
            int temp = l1->val+l2->val+carry;
            int result = temp%10;
            carry = temp/10;
         
            iterator->next = new ListNode(result);
            iterator = iterator->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        if(l1==NULL)
        {
            while(l2!=NULL)
            {
                int temp2 = l2->val+carry;
                int result2 = temp2%10;
                carry = temp2/10;
                iterator->next = new ListNode(result2);
                iterator = iterator->next;
                l2 = l2->next;
            }
        }
        else if(l2==NULL)
        {
            while(l1!=NULL)
            {
                int temp2 = l1->val+carry;
                int result2 = temp2%10;
                carry = temp2/10;
                iterator->next = new ListNode(result2);
                iterator = iterator->next;
                l1 = l1->next;
            }            
        }
        
        if(carry!=0)
        {
            iterator->next = new ListNode(carry);
            iterator = iterator->next;
        }
        return begin.next;
    }
};


