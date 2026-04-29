# P-2: Student Highest GWA Finder
# Format: name : gwa per line in students.txt

file = open('student_record_processor/students.txt', 'r')
students = []

for line in file:
    line = line.strip()
    if ': ' in line:  # Valid line check
        name, gwa_str = line.split(' : ')
        gwa = float(gwa_str)
        students.append((name, gwa))

file.close()

if students:
    # Find highest GWA
    best_student = max(students, key=lambda x: x[1])
    print(f"{best_student[0]} got the highest GWA: {best_student[1]}")
else:
    print("No valid student data found!")