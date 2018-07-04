///You are given two non-empty linked lists representing two non-negative integers. 
///The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
///You may assume the two numbers do not contain any leading zero, except the number 0 itself.

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

///pretty elementary math, just take care of the carry number and check which linked list is not exhausted
