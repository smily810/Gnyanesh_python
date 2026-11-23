def add_student(students, roll_no, name, age, grade):
    students[roll_no] = {
        "name": name,
        "age": age,
        "grade": grade
    }


def remove_student(students, roll_no):
    if roll_no in students:
        del students[roll_no]
        print("Student removed successfully")
    else:
        print("Student not found")


def student_records():
    students = {}

    add_student(students, 101, "Ravi", 18, "A")
    add_student(students, 102, "Anil", 19, "B")
    add_student(students, 103, "Kishan", 18, "A+")

    print("Student Records:")
    print(students)

    remove_student(students, 102)

    print("After removing student 102:")
    print(students)


student_records()
