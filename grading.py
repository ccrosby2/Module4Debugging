#Cierra Crosby
#2/7/2024
#Instructor Antonio Tovar
#This program calculates grades in a course used in school
#This line of coding write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.
# This line of coding gives a Grade for each exam given in a course according to the following scale:
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F
#This program gives three average exams with passing score of 89,90,and 90 and prints a statement "Student is passing"
# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.
#This program gives three average exams with passing score of 50,51, and 0 and prints a statement "Student is failing"
# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int( input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))
print("Average: " + str(avg))
print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
