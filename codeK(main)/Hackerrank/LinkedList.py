# swap every adjacent
# 1 -> 2 -> 3 -> 4 will be 2 -> 1 -> 4 -> 3

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        current = self
        nodes = []
        while current:
            nodes.append(str(current.val))
            current = current.next
        return "->".join(nodes)

def swap(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        #prev-> 2 -> 1 -> 2
        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
    
    return dummy.next
    
    

    

test_list = ListNode("2", ListNode("1", ListNode("4", ListNode("3"))))
res = swap(test_list)
print(res)

