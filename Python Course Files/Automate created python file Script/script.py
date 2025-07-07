from pathlib import Path

# Get path safely
path = input("Enter folder path: ").strip()
folder = Path(path)

questions = {1 : "#Q1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one? ",
2: "#Q2. Write a program to input name, marks and phone number of a student and format it using the format function like below: “The name of the student is Harry, his marks are 72 and phone number is 99999888” ",
3: "#Q3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers. ",
4 : "#Q4. Write a program to filter a list of numbers which are divisible by 5. ",
5 : "#Q5. Write a program to find the maximum of the numbers in a list using the reduce function.",
6: "#Q6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv. ",
7: "#Q7. Explore the ‘Flask’ module and create a web server using Flask & Python. "   }
# Ensure path ends with slash and exists

how_much_files = int(input("Enter how many files to create: "))
chapter_no = int(input("Enter chapter number: "))

for i in range(1, how_much_files + 1):
    file_path = folder / f"{chapter_no}_problem_{i}.py"
    with open(file_path, "w") as file:
            file.write(f"Q : {questions[i]}")

print(f"✅ Successfully created {how_much_files} files in {folder}")
