# 9. Write a program to find out whether a file is identical & matches the content of
# another file.



with open("this.txt") as f: 
    file1 = f.read()

with open("this_copy.txt",) as f:
    file2 = f.read()

if(file1==file2): 
    print("Yes Both files store same content")

else: 
    print("NO Both files do not store same content")
