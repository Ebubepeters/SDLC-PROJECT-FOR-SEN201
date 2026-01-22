# SDLC-PROJECT-FOR-SEN201
SDLC PROJECT FOR SEN201
1. Planning / Requirements Gathering
•  Objective: Create a program that helps Nigerian university students calculate Semester GPA and Cumulative CGPA using the standard 5.0 grading scale.
•  Functional Requirements:
	•  Input number of semesters completed
	•  For each semester: input number of courses, then for each course → course code (optional), credit units (int/float), grade letter (A–F)
	•  Calculate GPA per semester
	•  Calculate overall CGPA
	•  Display class of degree recommendation (First Class, Second Class Upper, etc.)
	•  Handle invalid inputs gracefully
	•  Option to save/load data (simple text file for persistence)
•  Non-Functional Requirements: Console-based, no external libraries except built-in ones, easy to run, accurate for Nigerian 5.0 scale.
•  Grading Scale (5.0 – most Nigerian universities):
	•  A = 5.0 (70–100%)
	•  B = 4.0 (60–69%)
	•  C = 3.0 (50–59%)
	•  D = 2.0 (45–49%)
	•  E = 1.0 (40–44%)
	•  F = 0.0 (below 40%)
2. System Design
•  Architecture: Single-file console Python script
•  Data Structure:
	•  List of semesters, each semester is a dict: {"semester": int, "courses": list of {"code": str, "credits": float, "grade": str, "points": float}}
	•  Or simpler: track total_quality_points and total_credits cumulatively
•  Key Functions (names match code):
	•  get_grade_point(grade_letter)
	•  calculate_semester_gpa(courses)
	•  calculate_cgpa(semesters_data)
	•  get_class_of_degree(cgpa)
	•  main() — main menu and loop
•  File: cgpa_data.txt (optional save/load)
3. Testing
•  Test Case 1: 2 semesters, mix of A/B/C → expect CGPA between 3.5–4.5
•  Test Case 2: One semester with F grade → GPA drops
•  Edge cases: 0 courses, invalid grade input, 0 credits (handled)
•  Manual verification: Compare with online calculators or manual math
5. Deployment
•  Run locally: python cgpa_calculator.py
•  GitHub: Public repo for sharing/submission
6. Maintenance
•  Future: Add file save/load, GUI (Tkinter), support 4.0 scale (polytechnics), course code input, export to PDF


