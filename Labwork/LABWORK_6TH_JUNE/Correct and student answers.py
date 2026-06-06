# Correct and student answers
correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

# Part 1: Calculate score
score = 0

for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1

print("Score =", score)

# Part 2: Incorrect question numbers
print("Incorrect Questions:")

for i in range(len(correct)):
    if correct[i] != student[i]:
        print(i + 1)

# Part 3: Count correct and wrong answers
correct_count = score
wrong_count = len(correct) - score

print("Correct Answers =", correct_count)
print("Wrong Answers =", wrong_count)

# Part 4: Pass or Fail
percentage = (score / len(correct)) * 100

if percentage >= 60:
    print("Pass")
else:
    print("Fail")
