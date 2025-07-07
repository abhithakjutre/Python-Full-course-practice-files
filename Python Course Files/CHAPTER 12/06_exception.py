try: 
    a = int(input("Hey, Enter the user number : "))

    print(a)

except ValueError as e : 
    print(e)
    print("Hey")
except Exception as e: 
    print(e)


print("Thank You")