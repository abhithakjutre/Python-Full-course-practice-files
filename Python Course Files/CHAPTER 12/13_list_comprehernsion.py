myList = [1, 3, 5, 6, 3, 5]

squaredList = [] 
# for item in myList: 
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]
print(squaredList)