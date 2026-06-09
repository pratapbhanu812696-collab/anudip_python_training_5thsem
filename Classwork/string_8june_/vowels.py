#write a program to find out input a sentence and display the frequency of vowels which are present in given sentence ignoring the case of the characters

sentence = input("Enter a sentence: ")

a = e = i = o = u = 0

# Convert sentence to lowercase and check each character
for ch in sentence.lower():
    if ch == 'a':
        a += 1
    elif ch == 'e':
        e += 1
    elif ch == 'i':
        i += 1
    elif ch == 'o':
        o += 1
    elif ch == 'u':
        u += 1
        
# Display only those vowels whose frequency is greater than 0
print("Frequency of vowels:")

if a > 0:
    print("A =", a)
if e > 0:
    print("E =", e)
if i > 0:
    print("I =", i)
if o > 0:
    print("O =", o)
if u > 0:
    print("U =", u)
