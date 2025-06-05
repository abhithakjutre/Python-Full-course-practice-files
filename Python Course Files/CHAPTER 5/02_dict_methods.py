marks = { 
    "abhi": 90, 
    "yash": 95,
    "Deepak": 85,
    90: "ninety"
}

# Dictionary Methods for 'marks':

# 1. Get all keys from marks dictionary
print(marks.keys())  # Will print: dict_keys(['abhi', 'yash', 'Deepak', 90])

# 2. Get all values from marks dictionary
print(marks.values())  # Will print: dict_values([90, 95, 85, 'ninety'])

# 3. Safely get a value using get() method
print(marks.get("abhi"))  # Will print: 90
print(marks.get("unknown", "Not Found"))  # Will print: Not Found

# 4. Get all key-value pairs
print(marks.items())  # Will print: dict_items([('abhi', 90), ('yash', 95), ('Deepak', 85), (90, 'ninety')])

# 5. Update marks dictionary with new values
marks.update({"abhi": 89, "alok": 98})

# 3. values() - Get all values
values = marks.values()
print(list(values))  # [85, 90]

# 4. items() - Get key-value pairs
items = marks.items()
print(list(items))  # [('John', 85), ('Alice', 90)]

# 5. update() - Update dictionary with elements from another dictionary
marks.update({"Bob": 88, "Alice": 92})
print(marks)  # {'John': 85, 'Alice': 92, 'Bob': 88}

# 6. pop() - Remove specified key and return its value
removed_value = marks.pop("Bob")
print(removed_value)  # 88
print(marks)  # {'John': 85, 'Alice': 92}

# 7. clear() - Remove all items
marks.clear()
print(marks)  # {}

# 8. copy() - Create a shallow copy
original = {"a": 1, "b": 2}
copied = original.copy()
