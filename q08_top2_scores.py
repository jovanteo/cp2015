students = int(input("Number of students: "))
name = []
mark = []
while students != 0:
    name.append(input("Enter name of student: "))
    mark.append(int(input("Enter mark of student: ")))
    students -= 1
highest = max(mark)
print(name[mark.index(highest)], "has the highest score of:", highest)
name.pop(mark.index(highest))
mark.pop(mark.index(highest))
highest2 = max(mark)
print(name[mark.index(highest2)],"has the second highest score of:", highest2)
