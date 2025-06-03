# 2. Write a program to accept marks of 6 students and display them in a sorted  manner.

m1 = int(input("Enter the marks of student one  : "))
m2 = int(input("Enter the marks of student two  : "))
m3 = int(input("Enter the marks of student three  : "))
m4 = int(input("Enter the marks of student four : "))
m5 = int(input("Enter the marks of student five : "))
m6 = int(input("Enter the marks of student six   : "))

marks = [m1, m2, m3, m4, m5, m6]

marks.sort()
print(marks)