# Passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Part 1: Find busiest stop
highest = passengers[0]
stop = 1

for i in range(len(passengers)):
    if passengers[i] > highest:
        highest = passengers[i]
        stop = i + 1

print("Busiest Stop =", stop)

# Part 2: Stops with fewer than 10 passengers
print("Stops with less than 10 passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print(i + 1)

# Part 3: Average passengers
total = 0

for p in passengers:
    total += p

average = total / len(passengers)

print("Average Passengers =", average)

# Part 4: Check if any stop exceeded 25 passengers
found = False

for p in passengers:
    if p > 25:
        found = True
        break

if found:
    print("A stop exceeded 25 passengers")
else:
    print("No stop exceeded 25 passengers")
