class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()  # 虛擬頭節點（最後回傳 dummy.next）
        current = dummy
        carry = 0  # 初始進位為 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # 若 l1 空了就用 0
            val2 = l2.val if l2 else 0  # 若 l2 空了就用 0

            total = val1 + val2 + carry
            carry = total // 10  # 計算進位
            current.next = ListNode(total % 10)  # 取個位數存入新節點
            current = current.next

            # 前進到下一位
            print(l1.val, l2.val)
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# 🔧 工具：把 list 轉成 linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# 🔧 工具：把 linked list 轉成 list（用來印結果）
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == '__main__':
    l1 = list_to_linkedlist([2,4,3])
    l2 = list_to_linkedlist([5,6,4])
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))