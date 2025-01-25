student1 = input("Insert the first student ID: ")
student2 = input("Insert the second student ID: ")

id1 = int(student1[1:])
id2 = int(student2[1:])

if id1 > id2 :
    print(f"{student2}\n{student1}")
else :
    print(f"{student1}\n{student2}")