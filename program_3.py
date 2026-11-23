def student_list():
    students = ["Ravi", "Anil", "Kiran", "Varun"]

    print("Original list:", students)

    students.append("Suresh")
    print("After adding Suresh:", students)

    students.remove("Anil")
    print("After removing Anil:", students)

    students.sort()
    print("After sorting:", students)


student_list()
