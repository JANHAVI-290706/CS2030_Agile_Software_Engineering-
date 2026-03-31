# Dictionary to store courses and enrolled students
# Pair Programming Lab
# Driver (Iteration 1): Ananya
# Navigator (Iteration 1): Prateeksha
# Driver (Iteration 2): Prateeksha 
# Navigator (Iteration 2): Ananya
courses = {}

def add_course():
    course_name = input("Enter course name: ")

    if course_name in courses:
        print("Course already exists!")
    else:
        courses[course_name] = []
        print("Course added successfully!")


def enroll_student():
    course_name = input("Enter course name: ")

    if course_name not in courses:
        print("Course does not exist!")
        return

    student_name = input("Enter student name: ")

    if student_name in courses[course_name]:
        print("Student already enrolled in this course!")
    else:
        courses[course_name].append(student_name)
        print("Student enrolled successfully!")


def main():
    while True:
        print("\n--- Course Enrollment System ---")
        print("1. Add Course")
        print("2. Enroll Student")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_course()
        elif choice == "2":
            enroll_student()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
