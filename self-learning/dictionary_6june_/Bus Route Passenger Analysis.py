# Bus Route Passenger Analysis

passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# Task 1: Stops having more than 20 passengers
print("Stops with more than 20 passengers:")

for stop in passengers:
    if passengers[stop] > 20:
        print(stop)

# Task 2: Count stops with fewer than 10 passengers
count = 0

for stop in passengers:
    if passengers[stop] < 10:
        count += 1

print("Stops with fewer than 10 passengers =", count)

# Task 3: Find busiest stop
busy_stop = ""
max_passengers = 0

for stop in passengers:
    if passengers[stop] > max_passengers:
        max_passengers = passengers[stop]
        busy_stop = stop

print("Busiest Stop =", busy_stop)

# Task 4: Stops requiring extra bus
extra_bus = []

for stop in passengers:
    if passengers[stop] > 25:
        extra_bus.append(stop)

print(extra_bus)

# Task 5: Average passengers
total = 0

for stop in passengers:
    total += passengers[stop]

average = total / len(passengers)

print("Average Passengers =", average)
