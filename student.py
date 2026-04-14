def calGrade(value):
    if value >= 85 and value <= 100:
            result = 'A'
    elif value >= 70 and value < 85:
        result = 'B'
    elif value >= 35 and value < 70:
        result = 'C'
    elif value < 35 and value >= 0:
        result = 'Fail'
    else:
        result = "Invalid Percentage"
    
    return result


subjects = int(input("Enter Number of Subjects : "))
marks = int(input("How much marks the paper contain(eg. 100,50,25) : "))
students = []
flag = True

while(flag):
    print()
    print("------Student Management System------")
    print()
    print("1.Add Student")
    print("2.Delete Student")
    print("3.Show Student Details")
    print("4.Update Student")
    print("5.Save to File")
    print("6.Read Records from file")
    print("7.Exit")
    print()
    choice = int(input("Enter Your Choice : "))

    match(choice):
        case 1:
            name = input("Enter Student Name : ")
            roll = input("Enter PRN (23UETXXX) : ")

            student_marks = []   

            for i in range(1, subjects + 1):
                score = float(input(f"Enter Marks of Subject-{i} : "))
                student_marks.append(score)

            total = sum(student_marks)
            percentage = (total / (subjects * marks)) * 100
            grade = calGrade(percentage)

            student = {
                "name": name,
                "roll": roll,
                "marks": student_marks,
                "total": total,
                "percentage": percentage,
                "grade": grade
            }

            students.append(student)

            print("Student Added Successfully!")
            print()
            print(students)
            print()

        case 2:
            roll_no = input("Enter PRN to delete the record(23UETXXX) : ")
            found = False

            for s in students:
                if s["roll"] == roll_no:
                    students.remove(s)
                    print()
                    print("Student Record Deleted!!")
                    found = True
                    break

            if not found:
                print("Student Record Not Found!!")

        case 3:
            if len(students) == 0:
                print("No student Record Found!!")
            else:
                for s in students:
                    print()
                    print(f"Name : {s["name"]}")
                    print(f"Roll NO. : {s["roll"]}")
                    print(f"Marks : {s["marks"]}")
                    print(f"Total : {s["total"]}")
                    print(f"Percentage : {s["percentage"]}")
                    print(f"Grade : {s["grade"]}")
        
        case 4:
            roll_no = input("Enter PRN to Update Record(23UETXXX) : ")
            found = False

            for s in students:
                if s["roll"] == roll_no:
                    found = True
                    print()
                    print("What You want to Update : ")
                    print()
                    print("1.Name")
                    print("2.Roll No(PRN)")
                    print("3.Marks")
                    print()
                    update_choice = int(input("Enter Your Update Choice : "))

                    match(update_choice):
                        case 1:
                            new_name = input("Enter New Name : ")
                            s["name"] = new_name
                            print("Name Updated Successfully!!")
                            break

                        case 2:
                            new_roll = input("Enter New PRN(23UETXXX) : ")
                            s["roll"] = new_roll
                            print("PRN Updated Successfully!!")

                        case 3:
                            new_marks = []
                            print("Enter New Marks--")
                            for i in range(1,(subjects + 1)):
                                new_score = float(input(f"Enter marks of sunbject-{i} : "))
                                new_marks.append(new_score)

                            new_total = sum(new_marks)
                            new_percentage = (new_total / (subjects * marks)) * 100
                            new_grade = calGrade(new_percentage)

                            s["marks"] = new_marks
                            s["total"] = new_total
                            s["percentage"] = new_percentage
                            s["grade"] = new_grade

                            print("Marks Updated Successfully!!")

                        case _:
                            print("Invalid Choice, Try Again!!")

        case 5:
            file = open("Student_File.txt", "w")
            for s in students:
                file.write(f"Name = {s['name']}")
                file.write(f"\nRoll NO. : {s["roll"]}")
                file.write(f"\nMarks : {s["marks"]}")
                file.write(f"\nPercentage : {s["percentage"]}")
                file.write(f"\nGrade : {s["grade"]}")
                file.write("\n\n")

            file.close()
            print("Saved in file Successfully!!")

        case 6:
            file = open("Student_File.txt", "r")
            record = file.read()
            print(record)
            file.close()

        case 7:
            print("Terminating Program...!!")
            flag = False

        case _:
            print("Invalid Choice, Re-execute the Program!!")
            flag = False