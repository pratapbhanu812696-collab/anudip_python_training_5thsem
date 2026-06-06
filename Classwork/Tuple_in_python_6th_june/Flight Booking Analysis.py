# Flight Booking Analysis using tuples
bookings = (
("P101", "Delhi", "Confirmed"),
("P102", "Mumbai", "Waiting"),
("P103", "Delhi", "Confirmed"),
("P104", "Chennai", "Cancelled"),
("P105", "Mumbai", "Confirmed"),
("P106", "Delhi", "Waiting")
)

#1.Display all passengers whose booking status is Confirmed.
print("Passengers with Confirmed Booking:")
for booking in bookings:
    if booking[2] == "Confirmed":
        print(booking[0], "-", booking[1])


#2.Count the number of passengers travelling to Delhi.
delhi_count = 0
for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count += 1
print("\nNumber of passengers travelling to Delhi:", delhi_count)


#3.Count Confirmed, Waiting, and Cancelled bookings separately.
confirmed_count = 0
waiting_count = 0
cancelled_count = 0
for booking in bookings:
    if booking[2] == "Confirmed":
        confirmed_count += 1
    elif booking[2] == "Waiting":
        waiting_count += 1
    elif booking[2] == "Cancelled":
        cancelled_count += 1
print("\nBooking Status Counts:")
print("Confirmed:", confirmed_count)
print("Waiting:", waiting_count)
print("Cancelled:", cancelled_count)


#4.Create a list containing passenger IDs with Waiting status.
waiting_passengers = []
for booking in bookings:
    if booking[2] == "Waiting":
        waiting_passengers.append(booking[0])
print("\nPassenger IDs with Waiting Status:", waiting_passengers)

#5.Determine which destination has the highest number of bookings.
destination_counts = {}
for booking in bookings:
    destination = booking[1]
    if destination in destination_counts:
        destination_counts[destination] += 1
    else:
        destination_counts[destination] = 1

max_destination = max(destination_counts, key=destination_counts.get)
print("\nDestination with Highest Number of Bookings:", max_destination)
