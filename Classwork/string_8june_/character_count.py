#write a program to input a string from user and count the number of characters present in the string without using len function   
string = input("Enter a string: ")
char_count = 0
for char in string:
    char_count += 1
print("Number of characters in the string:", char_count)
