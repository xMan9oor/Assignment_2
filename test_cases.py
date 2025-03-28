
# test_cases.py
# This file include various test case to demonstrate the feature of the Royal Stay Hotel Management System
# Each test case is provided with two example

from hotel_classes import Hotel, SingleRoom, DoubleRoom, SuiteRoom, Guest, Booking, Payment, Invoice, Feedback

# Test case for Guest Account Creation
def test_guest_account_creation():

    # Example 1: Create a guest and print details

    guest1 = Guest("Ayesha", "ayesha@example.com", "1234567890", "Gold")
    print("Test Guest Account Creation 1: " + guest1.__str__())

    # Example 2: Create another guest and update loyalty points

    guest2 = Guest("Hamda", "hamda@example.com", "0987654321", "Silver")
    guest2.add_loyalty_points(50)
    print("Test Guest Account Creation 2: " + guest2.__str__())

# Test case for Searching for Available Rooms
def test_search_available_rooms():

    # Create sample rooms

    room1 = SingleRoom("101", ["Wi-Fi", "TV"], 100.0, "Queen", 1, "City View")
    room2 = DoubleRoom("102", ["Wi-Fi", "TV", "Mini-Bar"], 150.0, "King and Twin", 2, "Garden View")
    room3 = SuiteRoom("201", ["Wi-Fi", "TV", "Mini-Bar", "Jacuzzi"], 300.0, 3, "Luxury", "Breakfast included")

    # Mark room2 as not available

    room2.set_availability(False)

    # Hotel with rooms

    hotel = Hotel("Royal Stay", "123 Royal St")
    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)

    # Search available rooms: expect room1 and room3

    # Retrieve all room from the hotel

    all_rooms = hotel.get_rooms()

    # Filter room that are available

    available_rooms = []
    for room in all_rooms:
        if room.is_available():
            available_rooms.append(room)

    # Convert room object to string for display

    room_descriptions = []
    for room in available_rooms:
        room_descriptions.append(room.__str__())

    # Print the list of available room

    print("Test Search Available Rooms: " + " | ".join(room_descriptions))

    # Second example: Change availability and search again

    room3.set_availability(False)
    
    # Retrieve all rooms from the hotel
    all_rooms = hotel.get_rooms()

    # Filter available room

    available_rooms = []
    for room in all_rooms:
        if room.is_available():
            available_rooms.append(room)

    # Available room

    room_descriptions = []
    for room in available_rooms:
        room_descriptions.append(room.__str__())

    # Print the available room

    print("Test Search Available Rooms (Example 2): " + " | ".join(room_descriptions))

# Test case for Making a Room Reservation
def test_room_reservation():

    # Create a guest and a room

    guest = Guest("Mouza", "mouza@example.com", "1122334455", "Platinum")
    room = SingleRoom("103", ["Wi-Fi", "TV"], 120.0, "King", 1, "Ocean View")

    # Create a booking for the guest

    booking1 = Booking("B001", guest, room, "2025-04-01", "2025-04-05")
    guest.add_reservation(booking1)

    # Mark room as not available after booking

    room.set_availability(False)
    print("Test Room Reservation 1: " + booking1.__str__())

    # Second example: Another booking with different date

    room2 = DoubleRoom("104", ["Wi-Fi", "TV", "Mini-Bar"], 180.0, "Double", 2, "Pool View")
    booking2 = Booking("B002", guest, room2, "2025-05-10", "2025-05-15")
    guest.add_reservation(booking2)
    room2.set_availability(False)
    print("Test Room Reservation 2: " + booking2.__str__())

# Test case for Booking Confirmation Notification
def test_booking_confirmation_notification():

    # Simulate sending a notification after booking

    guest = Guest("Ali", "ali@example.com", "5566778899", "Gold")
    room = SuiteRoom("202", ["Wi-Fi", "TV", "Mini-Bar", "Jacuzzi"], 350.0, 3, "Premium", "All-inclusive")
    booking = Booking("B003", guest, room, "2025-06-01", "2025-06-07")

    # Notifications
    notification_msg = "Dear " + guest.get_name() + ", your booking " + booking.get_booking_id() + " has been confirmed."
    print("Test Booking Confirmation Notification 1: " + notification_msg)

    # Second example

    guest2 = Guest("Mohammed", "mohammed@example.com", "6677889900", "Silver")
    room2 = SingleRoom("105", ["Wi-Fi", "TV"], 110.0, "Queen", 1, "City View")
    booking2 = Booking("B004", guest2, room2, "2025-07-01", "2025-07-04")
    notification_msg2 = "Dear " + guest2.get_name() + ", your booking " + booking2.get_booking_id() + " has been confirmed"
    print("Test Booking Confirmation Notification 2: " + notification_msg2)

# Test case for Invoice Generation for a Booking
def test_invoice_generation():

    # Create a guest, room, and booking

    guest = Guest("Fatima", "fatima@example.com", "7788990011", "Platinum")
    room = DoubleRoom("106", ["Wi-Fi", "TV", "Mini-Bar"], 200.0, "King and Twin", 2, "Sea View")
    booking = Booking("B005", guest, room, "2025-08-01", "2025-08-05")

    # Charges include nightly rate and additional service fees

    charges = {"Nightly Rate": 200.0 * 4, "Service Fee": 50.0}
    invoice = Invoice("INV001", booking, charges)
    booking.set_invoice(invoice)
    print("Test Invoice Generation 1: " + invoice.__str__())

    # Second example: Another invoice

    charges2 = {"Nightly Rate": 180.0 * 3, "Cleaning Fee": 30.0, "Discount": -20.0}
    booking2 = Booking("B006", guest, room, "2025-09-10", "2025-09-13")
    invoice2 = Invoice("INV002", booking2, charges2)
    booking2.set_invoice(invoice2)
    print("Test Invoice Generation 2: " + invoice2.__str__())

# Test case for Processing Different Payment Methods
def test_payment_processing():

    # Process a credit card payment

    payment1 = Payment("Credit Card", 500.0, "TXN001")
    print("Test Payment Processing 1: " + payment1.__str__())

    # Process a mobile wallet payment

    payment2 = Payment("Mobile Wallet", 350.0, "TXN002")
    print("Test Payment Processing 2: " + payment2.__str__())

# Test case for Displaying Reservation History
def test_reservation_history():

    # Create a guest and add multiple booking

    guest = Guest("Hazza", "hazza@example.com", "3344556677", "Gold")
    room1 = SingleRoom("107", ["Wi-Fi", "TV"], 130.0, "Queen", 1, "Park View")
    room2 = DoubleRoom("108", ["Wi-Fi", "TV", "Mini-Bar"], 170.0, "Double", 2, "Garden View")
    booking1 = Booking("B007", guest, room1, "2025-10-01", "2025-10-03")
    booking2 = Booking("B008", guest, room2, "2025-11-05", "2025-11-09")
    guest.add_reservation(booking1)
    guest.add_reservation(booking2)
    history = guest.get_reservation_history()

    # Generate a list for booking history
    reservation_history = []
    for booking in history:
        reservation_history.append(booking.__str__())

    # Print the reservation history
    print("Test Reservation History 1: " + " | ".join(reservation_history))

    # Second example: Adding one more booking and displaying history

    room3 = SuiteRoom("209", ["Wi-Fi", "TV", "Mini-Bar", "Jacuzzi"], 400.0, 4, "Deluxe", "Spa Package")
    booking3 = Booking("B009", guest, room3, "2025-12-01", "2025-12-05")
    guest.add_reservation(booking3)
    history = guest.get_reservation_history()
    # Generate a list for booking history
    reservation_history = []
    for booking in history:
        reservation_history.append(str(booking))

    # Print the reservation history
    print("Test Reservation History 2: " + " | ".join(reservation_history))

# Test case for Cancellation of a Reservation
def test_cancellation_reservation():

    # Create a guest and a booking, then cancel the booking

    guest = Guest("Saif", "saif@example.com", "4455667788", "Silver")
    room = SingleRoom("110", ["Wi-Fi", "TV"], 115.0, "Queen", 1, "City View")
    booking = Booking("B010", guest, room, "2025-12-10", "2025-12-15")
    guest.add_reservation(booking)
    room.set_availability(False)

    # Simulate cancellation: update room availability and remove booking from guest history

    room.set_availability(True)
    guest.get_reservation_history().remove(booking)
    cancellation_msg = "Booking " + booking.get_booking_id() + " has been cancelled and room " + room.get_room_number() + " is now available"
    print("Test Cancellation of Reservation 1: " + cancellation_msg)

    # Second example: Another cancellation scenario

    room2 = DoubleRoom("111", ["Wi-Fi", "TV", "Mini-Bar"], 160.0, "Double", 2, "Garden View")
    booking2 = Booking("B011", guest, room2, "2025-12-20", "2025-12-25")
    guest.add_reservation(booking2)
    room2.set_availability(False)
    room2.set_availability(True)
    guest.get_reservation_history().remove(booking2)
    cancellation_msg2 = "Booking " + booking2.get_booking_id() + " has been cancelled and room " + room2.get_room_number() + " is now available"
    print("Test Cancellation of Reservation 2: " + cancellation_msg2)