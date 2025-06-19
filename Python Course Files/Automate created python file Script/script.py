from pathlib import Path

# Get path safely
path = input("Enter folder path: ").strip()
folder = Path(path)

# Ensure path ends with slash and exists

how_much_files = int(input("Enter how many files to create: "))
chapter_no = int(input("Enter chapter number: "))

for i in range(1, how_much_files + 1):
    file_path = folder / f"{chapter_no}_problem_{i}.py"
    with open(file_path, "w") as file:
            file.write(f"Q : {i}")

print(f"✅ Successfully created {how_much_files} files in {folder}")
