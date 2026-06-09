#write a program to input a sentence from user and count the number of special characters present in the sentence
sentence = input("Enter a sentence: ")
special_char_count = 0
for char in sentence:
    if not char.isalnum() and not char.isspace():
        special_char_count += 1
print("Number of special characters in the sentence:", special_char_count)
