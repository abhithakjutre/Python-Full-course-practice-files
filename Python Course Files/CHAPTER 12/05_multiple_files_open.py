
with (
    open("file1.txt", "w") as f1, 
    open("file2.txt", "w") as f2
): 
    f1.write("How are you what are you doing and i am not exsting so my name is file1")

    f2.write("Hello you are saying according for you and i am intersting so my name is file2")

with (
    open("file1.txt", "r") as fc1, 
    open("file2.txt", "r") as fc2
):

    content1 = fc1.read()
    print(content1)
    content2 = fc2.read()
    print(content2)