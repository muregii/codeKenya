
class CodeKenya:
    def __init__(self, name: str, role: str, age: int):
        self.name = name
        self.role = role
        self.age = age

    def __repr__(self):
        return f"name={self.name}, role={self.role}, age={self.age}"

raydon = CodeKenya("Raydon", "Instructor", 18)

print(raydon)
# arrays = [0, 1, 2, 3, 4]
# LinkedList (0, next) -> (1, next) -> (2)  0 -> 1 -> 2
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        if self.next:
            return f"{self.value} -> {self.next!r}"
        else:
            return f"{self.value}" 

z = Node(2)
y = Node(1, z)  
x = Node(0, y)

#nesting Node constructor calls.
x = Node(0, Node(1, Node(2)))

print(x)


# Merge Two Sorted Lists Blind 75
