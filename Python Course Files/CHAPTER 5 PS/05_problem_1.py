# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = { 
    "namaste": "Hello", 
    "dhanywad": "Thank you", 
    "krpya": "Please", 
    "madad": "help" 
}
word = input("Enter the word you want to look up  : ")
print(words[word])
