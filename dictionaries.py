students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Emma": 95
}

name = input("Enter the student's name : ")
if name in students:
    print(f"{name}'s marks : {students[name]}")
else:
    print(f'Student not found')

