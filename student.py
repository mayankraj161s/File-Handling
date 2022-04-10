# Write a program to get student data(roll no., name and marks) from user and write onto a binary file as long as user wants
import pickle
bfile = open("data.dat","wb+")
stu = {}
ans = 'y'
count = 0
while ans == 'y':
    rno = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    # adding data to dict stu{}
    stu['Rollno.'] = rno
    stu['Name'] = name
    stu['Marks'] = marks
    # now writing into a file
    pickle.dump(stu, bfile)
    ans = input("Want to enter more records? (y/n)... ")
    count += 1
print(count,"student added.")
bfile.close()
