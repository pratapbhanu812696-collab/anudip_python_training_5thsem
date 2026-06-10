def count_seats(seats):
    booked = seats.count("Booked")
    available = seats.count("Available")
    return booked, available

def first_available(seats):
    # index() finds the first occurrence. We add 1 for human seat number.
    if "Available" in seats:
        return seats.index("Available") + 1
    return -1

def occupancy_percentage(seats):
    booked = seats.count("Booked")
    total = len(seats)
    # Formula: (booked / total) * 100
    percentage = (booked / total) * 100
    return round(percentage, 2)

def display_available_seats(seats):
    print("Available Seat Numbers:")
    for index in range(len(seats)):
        if seats[index] == "Available":
            print(index + 1, end=" ")
    print() # For a new line at the end

# --- Main Program Execution ---
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# 1. Count Seats
booked_count, available_count = count_seats(seats)
print(f"Booked Seats: {booked_count}")
print(f"Available Seats: {available_count}")

# 2. First Available
print(f"First Available Seat: {first_available(seats)}")

# 3. Occupancy Percentage
print(f"Occupancy Percentage: {occupancy_percentage(seats)}%")

# 4. Display Available Seats
display_available_seats(seats)
