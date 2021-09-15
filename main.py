# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sumOfHeights = 0
for height in student_heights:
  sumOfHeights += height
print(sumOfHeights)

numberOfStudents = 0
for student in student_heights:
  numberOfStudents += 1
print(round(sumOfHeights/numberOfStudents))

