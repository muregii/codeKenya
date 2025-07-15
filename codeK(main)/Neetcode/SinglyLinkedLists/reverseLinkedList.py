def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev