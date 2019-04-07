class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ans = ListNode(0)
        while l1 or l2:
            Sum = carry
            if l1:
                Sum, l1 = Sum + l1.val, l1.next
            if l2:
                Sum, l2 = Sum + l2.val, l2.next
            
            carry = 1 if Sum >= 10 else 0
            Sum = (Sum - 10) if Sum >= 10 else Sum
            ans.next = ListNode(Sum)
            ans = ans.next
        return ans.next
        
s = Solution()

        
s = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
s.addTwoNumbers(l1, l2)