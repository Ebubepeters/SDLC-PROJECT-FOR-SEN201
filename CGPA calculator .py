def get_grade_point(grade):
    grade = grade.upper().strip()
    points = {
        'A': 5.0,
        'B': 4.0,
        'C': 3.0,
        'D': 2.0,
        'E': 1.0,
        'F': 0.0
    }
    return points.get(grade, None)

def calculate_semester_gpa(courses):
    if not courses:
        return 0.0, 0
    total_points = 0.0
    total_credits = 0.0
    for course in courses:
        credits = course['credits']
        points = course['points']
        total_points += credits * points
        total_credits += credits
    if total_credits == 0:
        return 0.0, 0
    return round(total_points / total_credits, 2), int(total_credits)

def calculate_cgpa(semesters):
    if not semesters:
        return 0.0, 0
    total_quality_points = 0.0
    total_credits_all = 0.0
    for sem in semesters:
        total_quality_points += sem['quality_points']
        total_credits_all += sem['credits']
    if total_credits_all == 0:
        return 0.0, 0
    return round(total_quality_points / total_credits_all, 2), int(total_credits_all)

def get_class_of_degree(cgpa):
    if cgpa >= 4.50:
        return "First Class Honours"
    elif cgpa >= 3.50:
        return "Second Class Honours (Upper Division)"
    elif cgpa >= 2.40:
        return "Second Class Honours (Lower Division)"
    elif cgpa >= 1.50:
        return "Third Class Honours"
    elif cgpa >= 1.00:
        return "Pass"
    else:
        return "Fail / Withdrawn"

def main():
    print("=== Nigerian University CGPA Calculator (5.0 Scale) ===")
    print("Enter grades: A=5.0, B=4.0, C=3.0, D=2.0, E=1.0, F=0.0\n")
    
    semesters = []
    total_semesters = int(input("How many semesters have you completed? "))
    
    for sem_num in range(1, total_semesters + 1):
        print(f"\n--- Semester {sem_num} ---")
        num_courses = int(input("Number of courses in this semester: "))
        courses = []
        
        for i in range(1, num_courses + 1):
            print(f"Course {i}:")
            # code = input("  Course code (optional): ").strip()
            while True:
                try:
                    credits = float(input("  Credit units: "))
                    if credits <= 0:
                        print("Credits must be positive.")
                        continue
                    break
                except ValueError:
                    print("Enter a valid number.")
            
            while True:
                grade_letter = input("  Grade (A/B/C/D/E/F): ").strip().upper()
                point = get_grade_point(grade_letter)
                if point is not None:
                    break
                print("Invalid grade. Use A, B, C, D, E, F.")
            
            courses.append({
                'credits': credits,
                'grade': grade_letter,
                'points': point
            })
        
        gpa, sem_credits = calculate_semester_gpa(courses)
        quality_points = gpa * sem_credits
        
        semesters.append({
            'semester': sem_num,
            'gpa': gpa,
            'credits': sem_credits,
            'quality_points': quality_points
        })
        
        print(f"Semester {sem_num} GPA: {gpa:.2f}  |  Credits: {sem_credits}")
    
    cgpa, total_credits = calculate_cgpa(semesters)
    degree_class = get_class_of_degree(cgpa)
    
    print("\n" + "="*50)
    print(f"FINAL CGPA: {cgpa:.2f}")
    print(f"Total Credits Earned: {total_credits}")
    print(f"Class of Degree: {degree_class}")
    print("="*50)

if __name__ == "__main__":
    while True:
        main()
        again = input("\nCalculate again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye! Keep pushing for that First Class")
            break
