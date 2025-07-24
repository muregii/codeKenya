class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next:
            return f"{self.val} -> {self.next!r}"
        else:
            return f"{self.val}"
        
#Build a LinkedList class
#More OOP practice
class LinkedList:

    def __init__(self, val=None):
        self.head = None
        if val:
            for v in val:
                self.append(v)

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def to_list(self):
        vals, curr = [], self.head
        while curr:
            vals.append(curr.value)
            curr = curr.next
        return vals

    def __repr__(self):
        return f"{self.to_list()}"


def mergeTwoLists(l1, l2):
    #1. Base Case
    if not l1 or not l2:
        return l1 or l2
    #2 Recursive case
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2
    
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
result = mergeTwoLists(l1, l2)
print(result)


"""💡 Key Idea
We recursively build the merged list by always picking the smaller node between l1 and l2, and then recursively merging the rest.

✅ Base Case
python
Copy
Edit
if not l1 or not l2:
    return l1 or l2
If either list is empty, return the other.

If l1 is None, we return l2 (since there’s nothing to merge from l1)

If l2 is None, we return l1

💬 Think of this as the "ending condition" — when there's nothing left to merge in one list, the rest of the other list just gets appended.

🔁 Recursive Step
Compare values:
python
Copy
Edit
if l1.val < l2.val:
Pick the smaller node to go first in the merged list.

Suppose l1.val is smaller...

Set l1.next to the result of merging the rest:
python
Copy
Edit
l1.next = mergeTwoLists(l1.next, l2)
You’ve chosen l1 as the head.

Now you merge the rest of l1 with l2, and attach that to l1.next.

Return the node you picked:
python
Copy
Edit
return l1
Otherwise (i.e., l2.val <= l1.val):
python
Copy
Edit
l2.next = mergeTwoLists(l1, l2.next)
return l2

🧠 Visual Example
Suppose:

plaintext
Copy
Edit
l1: 1 → 3 → 5  
l2: 2 → 4 → 6
The recursion unfolds like:

plaintext
Copy
Edit
1 < 2 → pick 1 → l1.next = merge(3 → 5, 2 → 4 → 6)
2 < 3 → pick 2 → l2.next = merge(3 → 5, 4 → 6)
3 < 4 → pick 3 → l1.next = merge(5, 4 → 6)
4 < 5 → pick 4 → l2.next = merge(5, 6)
5 < 6 → pick 5 → l1.next = merge(None, 6)
Base case → return 6
Final merged list:

plaintext
Copy
Edit
1 → 2 → 3 → 4 → 5 → 6
📌 Summary
The function works by always choosing the smaller head, and recursively solving the smaller problem of merging the rest.

The recursion builds the new list backward, as the call stack unwinds.

This is a classic example of divide and conquer + recursion with linked lists.

Stack Unwinds (Backtracking Begins)
Now we return and connect the nodes:

sql
Copy
Edit
merge(None, 6) → returns 6

merge(5, 6)
→ 5.next = 6
→ returns 5 → 6

merge(5, 4 → 6)
→ 4.next = (5 → 6)
→ returns 4 → 5 → 6

merge(3 → 5, 4 → 6)
→ 3.next = (4 → 5 → 6)
→ returns 3 → 4 → 5 → 6

merge(3 → 5, 2 → 4 → 6)
→ 2.next = (3 → 4 → 5 → 6)
→ returns 2 → 3 → 4 → 5 → 6

merge(1 → 3 → 5, 2 → 4 → 6)
→ 1.next = (2 → 3 → 4 → 5 → 6)
→ returns 1 → 2 → 3 → 4 → 5 → 6
✅ Final Merged List:
Copy
Edit
1 → 2 → 3 → 4 → 5 → 6

"""

