# 9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 

s = {8, 7, 12, "Harry", [1,2]} 

print(type(s)) # This will raise an error because lists are not hashable and cannot be added to a set.
