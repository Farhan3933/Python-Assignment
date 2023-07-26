def grade_student(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

def validate_marks():
    while True:
        try:
            marks = float(input("Enter the marks obtained by the student: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def main():
    print("Student Grading Program")

    while True:
        marks = validate_marks()
        grade = grade_student(marks)
        print(f"Grade: {grade}")

        choice = input("Do you want to calculate grade for another student? (y/n): ").lower()
        if choice != "y":
            break

if __name__ == "__main__":
    main()
