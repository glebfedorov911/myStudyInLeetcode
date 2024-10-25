class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        l1_list = self.read_l(l1)
        l2_list = self.read_l(l2)
        new_list = self.new_l(self.sum_l(l1_list, l2_list))
        return self.create_new_listnode(new_list)

    @staticmethod
    def read_l(l):
        l_list = []
        while l is not None:
            l_list.append(l.val)
            l = l.next
        return l_list
    
    def sum_l(self, l1, l2):
        l1_num = self.concat_num(l1)[::-1]
        l2_num = self.concat_num(l2)[::-1]
        return int(l1_num) + int(l2_num)

    @staticmethod
    def concat_num(l):
        sl = ''
        for num in l:
            sl += str(num)
        return sl
    
    @staticmethod
    def new_l(num):
        return [int(i) for i in str(num)]

    @staticmethod
    def create_new_listnode(l):
        for i in range(len(l)):
            if i == 0: 
                res = ListNode(l[i])
            else:
                res = ListNode(l[i], res)
        return res

# l1 = ListNode(2)
# l1 = ListNode(4, l1)
# l1 = ListNode(3, l1)

# l2 = ListNode(5)
# l2 = ListNode(6, l2)
# l2 = ListNode(4, l2)

# l1 = ListNode(0)

# l2 = ListNode(0)

# l1 = ListNode(9)
# l1 = ListNode(9, l1)
# l1 = ListNode(9, l1)
# l1 = ListNode(9, l1)
# l1 = ListNode(9, l1)
# l1 = ListNode(9, l1)
# l1 = ListNode(9, l1)

# l2 = ListNode(9)
# l2 = ListNode(9, l2)
# l2 = ListNode(9, l2)
# l2 = ListNode(9, l2)

# sol = Solution()
# print(sol.addTwoNumbers(l1, l2).val)
# print(sol.addTwoNumbers(l1, l2).next.val)
# print(sol.addTwoNumbers(l1, l2).next.next.val)
# print(sol.addTwoNumbers(l1, l2).next.next.next.val)
# print(sol.addTwoNumbers(l1, l2).next.next.next.next.val)
# print(sol.addTwoNumbers(l1, l2).next.next.next.next.next.val)
# print(sol.addTwoNumbers(l1, l2).next.next.next.next.next.next.val)
# print(sol.addTwoNumbers(l1, l2).next.next.next.next.next.next.next.val)