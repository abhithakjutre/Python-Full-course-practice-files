# 7. Write a program to find out the line number where python is present from ques 6.

with open("log.txt", "r") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
        if "Python" in line:
            print(f"Python is present in line no. {lineno} ")
            break
        lineno +=1
else:
        print("No Python is not present in the log file.")