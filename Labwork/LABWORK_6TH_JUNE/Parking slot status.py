# Parking slot status
slots = [1, 0, 1, 1, 0, 0, 1, 0]

# Part 1: Count occupied and available slots
occupied = 0
available = 0

for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied Slots =", occupied)
print("Available Slots =", available)

# Part 2: Find first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        print("First Available Slot =", i + 1)
        break

# Part 3: Display all available slot numbers
print("Available Slot Numbers:")
for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1)

# Part 4: Check occupancy above 75%
occupancy = (occupied / len(slots)) * 100

if occupancy > 75:
    print("Parking Occupancy Exceeds 75%")
else:
    print("Parking Occupancy Does Not Exceed 75%")
