n = int(input("Enter the number of students: "))
records= []
for i in range(n):
    name = input("Enter student name: ")
    rollno = input("Enter roll number: ")
    marks = int(input("Enter total marks (out of 100) for {}: ".format(name)))
    records.append({'Name','RollNo', 'Marks'})
print('The records are',records)
for student in records:
    print(f"Name: {student['Name']}")
    print(f"Roll No: {student['Roll No']}")
    print(f"Total Marks: {student['Total Marks']}")
    print()



    max_marks_student = records[0]
    for student in records:
        if student["Total Marks"] > max_marks_student["Total Marks"]:
            max_marks_student = student
    
    print(max_marks_student)



    if max_marks_student:
        print("Student with Maximum Marks:")
        print(f"Name: {max_marks_student['Name']}")
        print(f"Roll No: {max_marks_student['Roll No']}")
        print(f"Total Marks: {max_marks_student['Total Marks']}")
    else:
        print("No student records found.")

#part 2 of the question
for i in range(len(records)):
        rank = 1
        for j in range(len(records)):
            if records[j]["Total Marks"] > records[i]["Total Marks"]:
                rank += 1
        records[i]["Rank"] = rank

    # Display student details in ascending order of ranks
print("Student Details in Ascending Order of Ranks:")
for rank in range(1, len(records) + 1):
    for student in records:
        if student["Rank"] == rank:
            print(f"Rank: {student['Rank']}")
            print(f"Name: {student['Name']}")
            print(f"Roll No: {student['Roll No']}")
            print(f"Total Marks: {student['Total Marks']}")
            print()
