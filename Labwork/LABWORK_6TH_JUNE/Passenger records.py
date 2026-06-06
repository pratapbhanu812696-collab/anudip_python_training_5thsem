# Passenger records
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# Part 1: Display waiting-list passengers
print("Waiting List Passengers:")

for p in passengers:
    if p[1] == "Waiting":
        print(p[0])

# Part 2: Count confirmed and waiting passengers
confirmed = 0
waiting = 0

for p in passengers:
    if p[1] == "Confirmed":
        confirmed += 1
    else:
        waiting += 1

print("Confirmed =", confirmed)
print("Waiting =", waiting)

# Part 3: Check specific passenger status
name = input("Enter passenger name: ")

for p in passengers:
    if p[0] == name and p[1] == "Confirmed":
        print("Ticket Confirmed")
        break

# Part 4: Create separate lists
confirmed_list = []
waiting_list = []

for p in passengers:
    if p[1] == "Confirmed":
        confirmed_list.append(p[0])
    else:
        waiting_list.append(p[0])

print("Confirmed List =", confirmed_list)
print("Waiting List =", waiting_list)
