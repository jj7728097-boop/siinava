# ============================================================
# PROG103 - PRINCIPLES OF STRUCTURED PROGRAMMING
# Assignment 1: Student Result Management Terminal System (SRMTS)
# Student: [Your Name] | Student ID: [Your ID]
# Examiner: Elijah Fullah
# Semester: 02 | March 2026 - July 2026
# SDG: SDG 4 - Quality Education
# ============================================================

# ---------- CONSTANTS ----------
PASS_MARK = 50
GRADE_A = 75
GRADE_B = 65
GRADE_C = 55
GRADE_D = 45
MAX_SCORE = 100
MIN_SCORE = 0

# ---------- GLOBAL STORAGE ----------
students = []


# ============================================================
# FUNCTION 1: Add a student record
# ============================================================
def add_student():
    """Collects student details and subject scores, then stores the record."""
    print("\n" + "=" * 50)
    print("       ADD NEW STUDENT RECORD")
    print("=" * 50)

    name = input("Enter Student Name       : ").strip()
    student_id = input("Enter Student ID         : ").strip()

    if not name or not student_id:
        print("\n[ERROR] Name and Student ID cannot be empty.")
        return

    # Check for duplicate ID
    for s in students:
        if s["id"].lower() == student_id.lower():
            print(f"\n[ERROR] Student ID '{student_id}' already exists.")
            return

    print("\nEnter scores for 5 subjects (0 - 100):")
    subjects = ["Mathematics", "English", "Science", "ICT", "Social Studies"]
    scores = []

    for subject in subjects:
        while True:
            try:
                score = float(input(f"  {subject:<20}: "))
                if MIN_SCORE <= score <= MAX_SCORE:
                    scores.append(score)
                    break
                else:
                    print(f"  [ERROR] Score must be between {MIN_SCORE} and {MAX_SCORE}.")
            except ValueError:
                print("  [ERROR] Please enter a valid number.")

    # Calculate results
    average = calculate_average(scores)
    grade = assign_grade(average)
    status = "PASS" if average >= PASS_MARK else "FAIL"

    # Build record
    record = {
        "name": name,
        "id": student_id,
        "subjects": subjects,
        "scores": scores,
        "average": average,
        "grade": grade,
        "status": status
    }

    students.append(record)
    print(f"\n[SUCCESS] Record for '{name}' added successfully!")
    print(f"          Average: {average:.2f}% | Grade: {grade} | Status: {status}")


# ============================================================
# FUNCTION 2: Calculate average score
# ============================================================
def calculate_average(scores):
    """Returns the average of a list of scores."""
    if len(scores) == 0:
        return 0.0
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


# ============================================================
# FUNCTION 3: Assign a letter grade based on average
# ============================================================
def assign_grade(average):
    """Returns a letter grade based on the average score."""
    if average >= GRADE_A:
        return "A"
    elif average >= GRADE_B:
        return "B"
    elif average >= GRADE_C:
        return "C"
    elif average >= GRADE_D:
        return "D"
    else:
        return "F"


# ============================================================
# FUNCTION 4: View all student records
# ============================================================
def view_all_students():
    """Displays a summary table of all student records."""
    print("\n" + "=" * 65)
    print("              ALL STUDENT RECORDS")
    print("=" * 65)

    if len(students) == 0:
        print("  No student records found. Please add students first.")
        print("=" * 65)
        return

    print(f"  {'No.':<5} {'Name':<20} {'ID':<12} {'Avg%':<8} {'Grade':<7} {'Status'}")
    print("-" * 65)

    count = 1
    for s in students:
        print(f"  {count:<5} {s['name']:<20} {s['id']:<12} "
              f"{s['average']:<8.2f} {s['grade']:<7} {s['status']}")
        count += 1

    print("=" * 65)
    print(f"  Total Records: {len(students)}")


# ============================================================
# FUNCTION 5: Search for a specific student by ID
# ============================================================
def search_student():
    """Searches for a student by ID and displays their full result sheet."""
    print("\n" + "=" * 50)
    print("          SEARCH STUDENT RECORD")
    print("=" * 50)

    student_id = input("Enter Student ID to search: ").strip()
    found = False

    for s in students:
        if s["id"].lower() == student_id.lower():
            found = True
            display_result_sheet(s)
            break

    if not found:
        print(f"\n[NOT FOUND] No record found for ID: '{student_id}'")


# ============================================================
# FUNCTION 6: Display a formatted result sheet
# ============================================================
def display_result_sheet(s):
    """Prints a formatted result slip for a single student."""
    print("\n" + "=" * 50)
    print("        STUDENT RESULT SHEET")
    print("=" * 50)
    print(f"  Name       : {s['name']}")
    print(f"  Student ID : {s['id']}")
    print("-" * 50)
    print(f"  {'Subject':<22} {'Score':>6}   {'Remark'}")
    print("-" * 50)

    for i in range(len(s["subjects"])):
        score = s["scores"][i]
        remark = "Pass" if score >= PASS_MARK else "Fail"
        print(f"  {s['subjects'][i]:<22} {score:>6.1f}   {remark}")

    print("-" * 50)
    print(f"  {'Average Score':<22} {s['average']:>6.2f}")
    print(f"  {'Grade':<22} {s['grade']:>6}")
    print(f"  {'Overall Status':<22} {s['status']:>6}")
    print("=" * 50)


# ============================================================
# FUNCTION 7: Generate class performance summary
# ============================================================
def class_summary():
    """Calculates and displays overall class performance statistics."""
    print("\n" + "=" * 50)
    print("        CLASS PERFORMANCE SUMMARY")
    print("=" * 50)

    if len(students) == 0:
        print("  No records available for summary.")
        print("=" * 50)
        return

    total_avg = 0
    pass_count = 0
    fail_count = 0
    highest = students[0]
    lowest = students[0]

    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for s in students:
        total_avg += s["average"]

        if s["status"] == "PASS":
            pass_count += 1
        else:
            fail_count += 1

        if s["average"] > highest["average"]:
            highest = s
        if s["average"] < lowest["average"]:
            lowest = s

        grade_counts[s["grade"]] += 1

    class_avg = total_avg / len(students)

    print(f"  Total Students    : {len(students)}")
    print(f"  Class Average     : {class_avg:.2f}%")
    print(f"  Students Passed   : {pass_count}")
    print(f"  Students Failed   : {fail_count}")
    print(f"  Pass Rate         : {(pass_count / len(students)) * 100:.1f}%")
    print("-" * 50)
    print(f"  Top Student       : {highest['name']} ({highest['average']:.2f}%)")
    print(f"  Lowest Student    : {lowest['name']} ({lowest['average']:.2f}%)")
    print("-" * 50)
    print("  Grade Distribution:")
    for grade, count in grade_counts.items():
        bar = "#" * count
        print(f"    Grade {grade}: {count:>3}  {bar}")
    print("=" * 50)


# ============================================================
# FUNCTION 8: Delete a student record
# ============================================================
def delete_student():
    """Removes a student record by ID after confirmation."""
    print("\n" + "=" * 50)
    print("         DELETE STUDENT RECORD")
    print("=" * 50)

    student_id = input("Enter Student ID to delete: ").strip()

    for i in range(len(students)):
        if students[i]["id"].lower() == student_id.lower():
            name = students[i]["name"]
            confirm = input(f"  Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                students.pop(i)
                print(f"\n[SUCCESS] Record for '{name}' has been deleted.")
            else:
                print("\n[CANCELLED] Deletion cancelled.")
            return

    print(f"\n[NOT FOUND] No record found for ID: '{student_id}'")


# ============================================================
# FUNCTION 9: Display main menu
# ============================================================
def display_menu():
    """Prints the main menu options."""
    print("\n" + "=" * 50)
    print("   STUDENT RESULT MANAGEMENT TERMINAL SYSTEM")
    print("         Limkokwing University - Sierra Leone")
    print("=" * 50)
    print("  [1] Add Student Record")
    print("  [2] View All Students")
    print("  [3] Search Student by ID")
    print("  [4] Class Performance Summary")
    print("  [5] Delete Student Record")
    print("  [0] Exit System")
    print("=" * 50)


# ============================================================
# MAIN PROGRAM - Entry Point
# ============================================================
def main():
    """Main loop that drives the SRMTS application."""
    print("\n  Welcome to the Student Result Management Terminal System")
    print("  SDG 4: Quality Education - Empowering students through data\n")

    while True:
        display_menu()
        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_summary()
        elif choice == "5":
            delete_student()
        elif choice == "0":
            print("\n  Thank you for using SRMTS. Goodbye!")
            print("  Limkokwing University of Creative Technology - Sierra Leone\n")
            break
        else:
            print("\n  [ERROR] Invalid choice. Please select a valid option (0-5).")


# ============================================================
# Run the program
# ============================================================
if __name__ == "__main__":
    main()