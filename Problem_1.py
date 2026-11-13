Name = input("Enter student name: ")

Mathematics = int(input("Enter marks: "))
English = int(input("Enter marks: "))
Bangla = int(input("Enter marks: "))

Total = Mathematics + English + Bangla

Average = Total / 3

if Average > 79:
    grade = "A+"
elif Average > 69:
    grade = "A" 
elif Average > 59:
    grade = "B"
elif Average > 49:
    grade = "C"
else:
    grade = "F"

print(f"Student name: {Name}")
print(f"Total marks: {Total}")
print(f"Average: {Average}")
print(f"Grade: {grade}")