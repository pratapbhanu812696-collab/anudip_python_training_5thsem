#5. Bus Seat Reservation Analysis
# Initial bus seat layout (1 = Booked, 0 = Available)
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Initialize trackers
booked_count = 0
available_count = 0
available_seat_numbers = []
first_available_seat = None

# Process seats
for i in range(len(seats)):
    seat_status = seats[i]
    seat_number = i + 1  # Convert 0-based index to 1-based seat number
    
    if seat_status == 1:
        booked_count += 1
    else:
        available_count += 1
        available_seat_numbers.append(seat_number)
        
        # Find the first available seat and stop searching immediately if not found yet
        if first_available_seat is None:
            first_available_seat = seat_number

# Calculate occupancy percentage
total_seats = len(seats)
occupancy_percentage = (booked_count / total_seats) * 100

# Determine occupancy status
if occupancy_percentage > 70:
    status = "More Than 70% Occupied"
else:
    status = "Not More Than 70% Occupied"

# Display the results
print(f"Booked Seats: {booked_count}")
print(f"Available Seats: {available_count}")
print(f"First Available Seat: {first_available_seat}")
print(f"Available Seat Numbers: {available_seat_numbers}")
print(f"Bus Occupancy: {occupancy_percentage:.0f}%")
print(f"Status: {status}")# Initial bus seat layout (1 = Booked, 0 = Available)
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]


