class CodeKenya:
    def __init__(self, name: str, role: str, age: int):
        self.name = name
        self.role = role
        self.age = age

    def __repr__(self):
        return f"name={self.name}, role={self.role}, age={self.age}"

raydon = CodeKenya("Raydon", "Instructor", 18)

print(raydon)
    