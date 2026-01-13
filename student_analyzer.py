import csv
import os

# =============================================================================
# CONSTANTS & SETUP
# =============================================================================
FILE_NAME = "students.csv"
students_list = []  # Global list to store Student objects

# =============================================================================
# TASK 4: OBJECT-ORIENTED PROGRAMMING (5 Marks)
# =============================================================================
class Student:
    def __init__(self, id, name, midterm, final, assignment):
        """
    Description:

    Parameters
    ----------
    :param self: INSERT DESCRIPTION
    :type self: type
    :param id: INSERT DESCRIPTION
    :type id: type
    :param name: INSERT DESCRIPTION
    :type name: type
    :param midterm: INSERT DESCRIPTION
    :type midterm: type
    :param final: INSERT DESCRIPTION
    :type final: type
    :param assignment: INSERT DESCRIPTION
    :type assignment: type

    .
    """
        self.id = int(id)
        self.name = name
        self.midterm = float(midterm)
        self.final = float(final)
        self.assignment = float(assignment)
        self.final_score = 0.0
        self.grade = ""

    def compute_final(self):
        """
    Description:

    Parameters
    ----------
    :param self: INSERT DESCRIPTION
    :type self: type

    .
    """
        self.final_score = (0.4 * self.midterm) + (0.5 * self.final) + (0.1 * self.assignment)

    def compute_grade(self):
        """
    Description:

    Parameters
    ----------
    :param self: INSERT DESCRIPTION
    :type self: type

    .
    """
        if 85 <= self.final_score <= 100:
            self.grade = "A"
        elif 70 <= self.final_score < 85:
            self.grade = "B"
        elif 55 <= self.final_score < 70:
            self.grade = "C"
        elif 40 <= self.final_score < 55:
            self.grade = "D"
        else:
            self.grade = "F"

    def to_dict(self):
        """
    Description:

    Parameters
    ----------
    :param self: INSERT DESCRIPTION
    :type self: type

    .
    """
        return {
            "id": self.id,
            "name": self.name,
            "midterm": self.midterm,
            "final": self.final,
            "assignment": self.assignment,
            "final_score": round(self.final_score, 2),
            "grade": self.grade
        }

# =============================================================================
# TASK 3: FILE HANDLING (4 Marks)
# =============================================================================
def load_data():
    """
    Description:

    .
    """
    global students_list
    students_list.clear()
    
    # Requirement: Handle missing file errors using try/except
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Create object from CSV data
                student = Student(
                    id=row["id"],
                    name=row["name"],
                    midterm=row["midterm"],
                    final=row["final"],
                    assignment=row["assignment"]
                )
                # Recalculate to ensure state is correct
                student.compute_final()
                student.compute_grade()
                students_list.append(student)
        print(f"Data loaded successfully from {FILE_NAME}.")
    except FileNotFoundError:
        print("No previous data file found. Starting with an empty database.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")

def save_data():
    """
    Description:

    .
    """
    try:
        with open(FILE_NAME, mode='w', newline='') as file:
            fieldnames = ["id", "name", "midterm", "final", "assignment", "final_score", "grade"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students_list:
                writer.writerow(student.to_dict())
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

# =============================================================================
# TASK 2: FUNCTIONS FOR CORE OPERATIONS (5 Marks)
# =============================================================================
def add_student():
    """
    Description:

    .
    """
    print("\n--- Add New Student ---")
    try:
        s_id = int(input("Enter Student ID: "))
        # Check for duplicate ID
        for s in students_list:
            if s.id == s_id:
                print(f"Error: Student with ID {s_id} already exists.")
                return

        name = input("Enter Name: ")
        midterm = float(input("Enter Midterm Score (0-100): "))
        final = float(input("Enter Final Exam Score (0-100): "))
        assignment = float(input("Enter Assignment Score (0-100): "))

        # Integration of Task 4 Class
        new_student = Student(s_id, name, midterm, final, assignment)
        new_student.compute_final()  # Calculate score
        new_student.compute_grade()  # Determine grade
        
        students_list.append(new_student)
        print(f"Student {name} added successfully!")

    except ValueError:
        print("Invalid input! Please enter numbers for ID and Scores.")

def remove_student():
    """
    Description:

    .
    """
    print("\n--- Remove Student ---")
    try:
        s_id = int(input("Enter Student ID to remove: "))
        found = False
        for s in students_list:
            if s.id == s_id:
                students_list.remove(s)
                print(f"Student with ID {s_id} removed successfully.")
                found = True
                break
        if not found:
            print(f"Student with ID {s_id} not found.")
    except ValueError:
        print("Invalid ID format.")

def search_student():
    """
    Description:

    .
    """
    print("\n--- Search Student ---")
    try:
        s_id = int(input("Enter Student ID to search: "))
        found = False
        for s in students_list:
            if s.id == s_id:
                print("\nStudent Found:")
                print(f"ID: {s.id} | Name: {s.name}")
                print(f"Scores -> Midterm: {s.midterm}, Final: {s.final}, Assignment: {s.assignment}")
                print(f"Result -> Final Score: {s.final_score:.2f}, Grade: {s.grade}")
                found = True
                break
        if not found:
            print(f"Student with ID {s_id} not found.")
    except ValueError:
        print("Invalid ID format.")

def update_student():
    """
    Description:

    .
    """
    print("\n--- Update Student ---")
    try:
        s_id = int(input("Enter Student ID to update: "))
        student = None
        for s in students_list:
            if s.id == s_id:
                student = s
                break
        
        if student:
            print(f"Updating record for {student.name}. Press Enter to keep current value.")
            
            name = input(f"New Name ({student.name}): ")
            if name: student.name = name
            
            m = input(f"New Midterm ({student.midterm}): ")
            if m: student.midterm = float(m)
            
            f = input(f"New Final ({student.final}): ")
            if f: student.final = float(f)
            
            a = input(f"New Assignment ({student.assignment}): ")
            if a: student.assignment = float(a)
            
            # Re-compute after update
            student.compute_final()
            student.compute_grade()
            print("Student updated and grades re-calculated!")
        else:
            print(f"Student with ID {s_id} not found.")
    except ValueError:
        print("Invalid input values.")

def show_all_students():
    """
    Description:

    .
    """
    print("\n--- All Student Records ---")
    if not students_list:
        print("No records found.")
        return

    print(f"{'ID':<10} {'Name':<15} {'Final Score':<12} {'Grade':<5}")
    print("-" * 45)
    for s in students_list:
        print(f"{s.id:<10} {s.name:<15} {s.final_score:<12.2f} {s.grade:<5}")

# =============================================================================
# TASK 5: REPORTING & STATISTICS (6 Marks)
# =============================================================================
def generate_report():
    """
    Description:

    .
    """
    print("\n--- Class Performance Report ---")
    if not students_list:
        print("No data available to generate statistics.")
        return

    # Extract scores
    scores = [s.final_score for s in students_list]
    
    # a. Highest & Lowest
    highest = max(scores)
    lowest = min(scores)
    
    # b. Class Average
    average = sum(scores) / len(scores)
    
    # c. Grade Distribution
    grades = [s.grade for s in students_list]
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades:
        if g in grade_counts:
            grade_counts[g] += 1
            
    # d. Sorted List (Descending)
    sorted_students = sorted(students_list, key=lambda x: x.final_score, reverse=True)

    print(f"Total Students: {len(students_list)}")
    print(f"Highest Score:  {highest:.2f}")
    print(f"Lowest Score:   {lowest:.2f}")
    print(f"Class Average:  {average:.2f}")
    print("-" * 30)
    print(f"Grade Distribution: {grade_counts}")
    print("-" * 30)
    print("Top Performers (Sorted Descending):")
    for s in sorted_students:
        print(f"{s.name}: {s.final_score:.2f} ({s.grade})")

# =============================================================================
# TASK 6: BONUS OPTIONAL (5 Marks) - [IMPROVED VISUALIZATION]
# =============================================================================
def visualize_grades():
    """
    Description:

    .
    """
    print("\n" + "="*45)
    print("      GRADE VISUALIZATION DASHBOARD      ")
    print("="*45)
    
    if not students_list:
        print("No data to visualize.")
        return
        
    grades = [s.grade for s in students_list]
    total_students = len(grades)
    categories = ["A", "B", "C", "D", "F"]
    
    # ANSI Color Codes for VS Code Terminal
    # Green(A), Blue(B), Yellow(C), Magenta(D), Red(F)
    colors = {
        "A": "\033[92m", 
        "B": "\033[94m", 
        "C": "\033[93m", 
        "D": "\033[95m", 
        "F": "\033[91m", 
        "RESET": "\033[0m"
    }

    print(f"Total Students: {total_students}")
    print("-" * 45)
    
    for cat in categories:
        count = grades.count(cat)
        # Calculate Percentage
        percent = (count / total_students * 100) if total_students > 0 else 0.0
        
        # Create Bar
        bar = "█" * count
        
        # Apply Color
        color_code = colors.get(cat, "")
        reset = colors["RESET"]
        
        # Print: Grade | Bar | Count (Percentage%)
        print(f" {color_code}{cat} | {bar} {count} ({percent:.1f}%){reset}")
        
    print("-" * 45)
    print("Note: Colors work best in VS Code Terminal.")

# =============================================================================
# MAIN SYSTEM LOOP
# =============================================================================
def main():
    """
    Description:

    .
    """
    load_data()  # Task 3: Load on startup
    
    # MENU SIRF EK BAAR SHOW HOGA (LOOP SE BAHAR)
    print("=============================================================")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Show All Students")
    print("6. Generate Report (Stats)")
    print("7. Grade Visualization (Bonus)")
    print("8. Exit")
    
    while True:
        # Loop mein sirf choice maangega, poora menu print nahi karega
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            show_all_students()
        elif choice == '6':
            generate_report()
        elif choice == '7':
            visualize_grades()  # New Colorful Version
        elif choice == '8':
            save_data()  # Task 3: Save on exit
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()