
# hotel_classes.py 
# This file contain all class definition for the Royal Stay Hotel Management System.

# ------------------------------ #
#           Hotel Class
# ------------------------------ #
class Hotel:
    
    # Hotel class represent the hotel entity.
    # Attributes:
        # _name (str): The name of the hotel
        # _address (str): The hotel address
        # _rooms (list): A list to store Room objects
        # _guests (list): A list to store Guest objects
        # _bookings (list): A list to store Booking objects
    
    def __init__(self, name, address):
        # Initialize hotel attribute
        self._name = name  # Hotel name (protected attribute)
        self._address = address  # Hotel address (protected attribute)
        self._rooms = []  # List to store room object
        self._guests = []  # List to store guest object
        self._bookings = []  # List to store booking object

    # Getter and setter method
    def get_name(self):
        # Return hotel name
        return self._name

    def set_name(self, name):
        # Set hotel name
        self._name = "Hotel " + name

    def get_address(self):
        # Return hotel addres
        return self._address

    def set_address(self, address):
        # Set hotel address
        self._address = address

    def add_room(self, room):
        # Append a room to the hotel room list
        self._rooms.append(room)

    def get_rooms(self):
        # Return the list of rooms
        return self._rooms

    def add_guest(self, guest):
        # Append a guest to the hotel guest list
        self._guests.append(guest)

    def get_guests(self):
        # Return the list of guest
        return self._guests

    def add_booking(self, booking):
        # Append a booking to the hotel booking list
        self._bookings.append(booking)

    def get_bookings(self):
        # Return the list of booking
        return self._bookings

    def __str__(self):
        # Return hotel information
        return "Hotel Name: " + self._name + " | Address: " + self._address

# ------------------------------ #
#           Room Classes
# ------------------------------ #
class Room:
    
    # Room class represents a generic room
    # Attributes:
        # _room_number (str): Room number
        # _room_type (str): Type of room
        # _amenities (list): List of amenities
        # _price_per_night (float): Price per night
        # _is_available (bool): Availability status
    
    def __init__(self, room_number, room_type, amenities, price_per_night, is_available=True):
        # Initialize room attribute
        self._room_number = room_number  # Protected attribute for room number
        self._room_type = room_type  # Protected attribute for room type
        self._amenities = amenities  # Protected attribute for amenities list
        self._price_per_night = price_per_night  # Protected attribute for price per night
        self._is_available = is_available  # Protected attribute for availability status

    # Getter method to retrieve the room number
    def get_room_number(self):
        return self._room_number

    # Setter method to update the room number
    def set_room_number(self, room_number):
        self._room_number = room_number

    # Getter method to retrieve the type of the room (single, double, suite)
    def get_room_type(self):
        return self._room_type

    # Setter method to update the room type
    def set_room_type(self, room_type):
        self._room_type = room_type

    # Getter method to retrieve the list of amenities available in the room
    def get_amenities(self):
        return self._amenities

    # Setter method to update the amenities list for the room
    def set_amenities(self, amenities):
        self._amenities = amenities

    # Getter method to retrieve the price per night for the room
    def get_price_per_night(self):
        return self._price_per_night

    # Setter method to update the price per night for the room
    def set_price_per_night(self, price):
        self._price_per_night = price

    # Getter method to check whether the room is available for booking
    def is_available(self):
        return self._is_available

    # Setter method to update the availability status of the room
    def set_availability(self, status):
        self._is_available = status

    def __str__(self):
        # Return room detail
        return "Room " + str(self._room_number) + " (" + self._room_type + ") | Price: $" + str(self._price_per_night)

# Child class for Single Room inheriting from Room
class SingleRoom(Room):
    
    # SingleRoom class inherits from Room
    # Additional Attributes:
        # _bed_type (str): Type of bed
        # _capacity (int): Maximum occupancy
        # _view (str): View from the room
    
    def __init__(self, room_number, amenities, price_per_night, bed_type, capacity, view, is_available=True):
        # Call parent constructor with room type as Single
        super().__init__(room_number, "Single", amenities, price_per_night, is_available)
        self._bed_type = bed_type  # Additional attribute for bed type
        self._capacity = capacity  # Additional attribute for capacity
        self._view = view  # Additional attribute for view

    # Getter method to retrieve the type of bed in the room (King, Queen, Twin)
    def get_bed_type(self):
        return self._bed_type

    # Setter method to update the bed type in the room
    def set_bed_type(self, bed_type):
        self._bed_type = bed_type

    # Getter method to retrieve the maximum number of people the room can accommodate
    def get_capacity(self):
        return self._capacity

    # Setter method to update the room capacity number of people allowed
    def set_capacity(self, capacity):
        self._capacity = capacity

    # Getter method to retrieve the view from the room (Sea View, City View, Garden View)
    def get_view(self):
        return self._view

    # Setter method to update the view description for the room
    def set_view(self, view):
        self._view = view


    def __str__(self):
        # Return details of single room
        return super().__str__() + " | Bed: " + self._bed_type + " | Capacity: " + str(self._capacity) + " | View: " + self._view

# Child class for Double Room inheriting from Room
class DoubleRoom(Room):
    
    # DoubleRoom class inherits from Room
    # Additional Attributes:
        # _bed_types (str): Types of beds available
        # _capacity (int): Maximum occupancy
        # _extra_features (str): Extra features available
   
    def __init__(self, room_number, amenities, price_per_night, bed_types, capacity, extra_features, is_available=True):
        # Call parent constructor with room type as "Double"
        super().__init__(room_number, "Double", amenities, price_per_night, is_available)
        self._bed_types = bed_types  # Additional attribute for bed type
        self._capacity = capacity  # Additional attribute for capacity
        self._extra_features = extra_features  # Additional attribute for extra feature

    # Getter method to retrieve the types of beds available in the room (King, Queen, Twin)
    def get_bed_types(self):
        return self._bed_types

    # Setter method to update the types of beds available in the room
    def set_bed_types(self, bed_types):
        self._bed_types = bed_types

    # Getter method to retrieve the maximum number of guests the room can accommodate
    def get_capacity(self):
        return self._capacity

    # Setter method to update the room's capacity (number of guests allowed)
    def set_capacity(self, capacity):
        self._capacity = capacity

    # Getter method to retrieve any extra features available in the room (Jacuzzi, Balcony, Smart TV)
    def get_extra_features(self):
        return self._extra_features

    # Setter method to update the extra features available in the room
    def set_extra_features(self, extra_features):
        self._extra_features = extra_features

    def __str__(self):
        # Return details for double room
        return super().__str__() + " | Beds: " + self._bed_types + " | Capacity: " + str(self._capacity) + " | Features: " + self._extra_features

# Child class for Suite Room inheriting from Room
class SuiteRoom(Room):
    
    # SuiteRoom class inherits from Room
    # Additional Attributes:
        # _number_of_rooms (int): Number of rooms in the suite
        # _luxury_level (str): Luxury level description
        # _service_included (str): Services included
    
    def __init__(self, room_number, amenities, price_per_night, number_of_rooms, luxury_level, service_included, is_available=True):
        # Call parent constructor with room type as Suite
        super().__init__(room_number, "Suite", amenities, price_per_night, is_available)
        self._number_of_rooms = number_of_rooms  # Additional attribute for number of room
        self._luxury_level = luxury_level  # Additional attribute for luxury level
        self._service_included = service_included  # Additional attribute for included service

    # Getter method to retrieve the total number of rooms available in the hotel
    def get_number_of_rooms(self):
        return self._number_of_rooms

    # Setter method to update the total number of rooms in the hotel
    def set_number_of_rooms(self, number):
        self._number_of_rooms = number

    # Getter method to retrieve the luxury level of the room (Standard, Deluxe, Suite)
    def get_luxury_level(self):
        return self._luxury_level

    # Setter method to update the luxury level of the room
    def set_luxury_level(self, level):
        self._luxury_level = level

    # Getter method to check which services are included with the room (Breakfast, Spa, Airport Pickup)
    def get_service_included(self):
        return self._service_included

    # Setter method to update the services included with the room
    def set_service_included(self, service):
        self._service_included = service

    def __str__(self):
        # Return details for suite room
        return super().__str__() + " | Rooms: " + str(self._number_of_rooms) + " | Luxury: " + self._luxury_level + " | Services: " + self._service_included

# ------------------------------ #
#    Person and Guest Classes
# ------------------------------ #
class Person:
    
    # Person class represents a generic person
    # Attributes (protected):
        # _name (str): Person's name
        # _email (str): Person's email
        # _contact (str): Contact information
    
    def __init__(self, name, email, contact):
        # Initialize person attributes
        self._name = name  # Protected attribute for name
        self._email = email  # Protected attribute for email
        self._contact = contact  # Protected attribute for contact

    # Getter method to retrieve the guest name
    def get_name(self):
        return self._name

    # Setter method to update the guest name
    def set_name(self, name):
        self._name = name

    # Getter method to retrieve the guest email address
    def get_email(self):
        return self._email

    # Setter method to update the guest email address
    def set_email(self, email):
        self._email = email

    # Getter method to retrieve the guest contact number
    def get_contact(self):
        return self._contact

    # Setter method to update the guest contact number
    def set_contact(self, contact):
        self._contact = contact

    def __str__(self):
        # Return person details
        return "Name: " + self._name + " | Email: " + self._email + " | Contact: " + self._contact

# Guest class inherit from Person and add loyalty detail and reservation history
class Guest(Person):
    
    # Guest class inherits from Person
    # Additional Attributes:
        # _loyalty_status (str): Loyalty status of the guest
        # _loyalty_points (int): Loyalty points accumulated
        # _reservation_history (list): List of past booking
    
    def __init__(self, name, email, contact, loyalty_status="Regular"):
        # Initialize the parent class attribute
        super().__init__(name, email, contact)
        self._loyalty_status = loyalty_status  # Additional attribute for loyalty status
        self._loyalty_points = 0  # Additional attribute for loyalty points
        self._reservation_history = []  # List to store reservation history

    # Getter and setter methods for additional attribute
    def get_loyalty_status(self):
        return self._loyalty_status

    def set_loyalty_status(self, status):
        self._loyalty_status = status

    def get_loyalty_points(self):
        return self._loyalty_points

    def add_loyalty_points(self, points):
        # Add loyalty points and update status message 
        self._loyalty_points += points

    def get_reservation_history(self):
        return self._reservation_history

    def add_reservation(self, booking):
        # Add a booking to the reservation history list
        self._reservation_history.append(booking)

    def __str__(self):
        # Return guest details 
        return super().__str__() + " | Loyalty Status: " + self._loyalty_status + " | Points: " + str(self._loyalty_points)

# ------------------------------ #
#         Booking Class
# ------------------------------ #
class Booking:
    
    # Booking class represents a room booking
    # Attributes:
        # _booking_id (str): Unique booking ID
        # _guest (Guest): The guest making the booking
        # _room (Room): The room booked
        # _check_in (str): Check-in date
        # _check_out (str): Check-out date
        # _invoice (Invoice): Invoice associated with the booking
    
    def __init__(self, booking_id, guest, room, check_in, check_out):
        # Initialize booking attribute
        self._booking_id = booking_id  # Unique booking id
        self._guest = guest  # Guest object for booking
        self._room = room  # Room object booked
        self._check_in = check_in  # Check in date as string
        self._check_out = check_out  # Check out date as string
        self._invoice = None  # Invoice will be generated later

    # Getter method to retrieve the booking ID
    def get_booking_id(self):
        return self._booking_id

    # Setter method to update the booking ID
    def set_booking_id(self, booking_id):
        self._booking_id = booking_id

    # Getter method to retrieve the guest associated with this booking
    def get_guest(self):
        return self._guest

    # Setter method to update the guest associated with this booking
    def set_guest(self, guest):
        self._guest = guest

    # Getter method to retrieve the room assigned for this booking
    def get_room(self):
        return self._room

    # Setter method to update the room assigned for this booking
    def set_room(self, room):
        self._room = room

    # Getter method to retrieve the check in date
    def get_check_in(self):
        return self._check_in

    # Setter method to update the check in date
    def set_check_in(self, check_in):
        self._check_in = check_in

    # Getter method to retrieve the check out date
    def get_check_out(self):
        return self._check_out

    # Setter method to update the check out date
    def set_check_out(self, check_out):
        self._check_out = check_out

    # Getter method to retrieve the invoice detail
    def get_invoice(self):
        return self._invoice

    # Setter method to update the invoice detail
    def set_invoice(self, invoice):
        self._invoice = invoice

    def __str__(self):
        # Return booking detail
        return "Booking ID: " + self._booking_id + " | Guest: " + self._guest.get_name() + " | Room: " + self._room.get_room_number() + " | Check-in: " + self._check_in + " | Check-out: " + self._check_out

# ------------------------------ #
#         Payment Class
# ------------------------------ #
class Payment:
    
    # Payment class represents a payment for a booking
    # Attributes:
        # _payment_method (str): Payment method used
        # _amount (float): Payment amount
        # _transaction_id (str): Transaction id
    
    def __init__(self, payment_method, amount, transaction_id):
        # Initialize payment attribute
        self._payment_method = payment_method  # Payment method (card, mobile wallet)
        self._amount = amount  # Payment amount
        self._transaction_id = transaction_id  # Unique transaction id

    # Getter and setter methods for payment attribute
    def get_payment_method(self):
        return self._payment_method

    def set_payment_method(self, method):
        self._payment_method = method

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    def get_transaction_id(self):
        return self._transaction_id

    def set_transaction_id(self, transaction_id):
        self._transaction_id = transaction_id

    def __str__(self):
        # Return payment details
        return "Payment Method: " + self._payment_method + " | Amount: $" + str(self._amount) + " | Transaction ID: " + self._transaction_id

# ------------------------------ #
#         Invoice Class
# ------------------------------ #
class Invoice:
    
    # Invoice class represents an invoice generated for a booking
    # Attributes:
        # _invoice_id (str): Unique invoice id
        # _booking (Booking): Associated booking
        # _charges (dict): Dictionary of charges
        # _total_amount (float): Total amount due
    
    def __init__(self, invoice_id, booking, charges):
        # Initialize invoice attribute
        self._invoice_id = invoice_id  # Unique invoice id
        self._booking = booking  # Booking object associated with the invoice
        self._charges = charges  # Dictionary containing charge detail
        self._total_amount = self.calculate_total()  # Calculate total amount using helper function

    def calculate_total(self):
        # Calculate the total amount from the charge dictionary
        total = 0.0  # Initialize total
        for charge in self._charges.values():
            total += charge  # Sum all charge
        return total

    # Getter and setter method for invoice attribute
    def get_invoice_id(self):
        return self._invoice_id

    def set_invoice_id(self, invoice_id):
        self._invoice_id = invoice_id

    def get_booking(self):
        return self._booking

    def set_booking(self, booking):
        self._booking = booking

    def get_charges(self):
        return self._charges

    def set_charges(self, charges):
        self._charges = charges
        self._total_amount = self.calculate_total()  # Recalculate total

    def get_total_amount(self):
        return self._total_amount

    def __str__(self):
        # Create a string for details of invoice
        details = "Invoice ID: " + self._invoice_id + " | Booking ID: " + self._booking.get_booking_id() + " | Total: $" + str(self._total_amount)
        return details

# ------------------------------ #
#         Feedback Class
# ------------------------------ #
class Feedback:
    
    # Feedback class represents feedback left by a guest
    # Attributes:
        # _feedback_id (str): Unique feedback id
        # _guest (Guest): Guest who left the feedback
        # _rating (int): Rating given by the guest
        # _comments (str): Additional comments

    def __init__(self, feedback_id, guest, rating, comments):
        # Initialize feedback attributes
        self._feedback_id = feedback_id  # Unique feedback id
        self._guest = guest  # Guest object
        self._rating = rating  # Rating given (Like 1-5)
        self._comments = comments  # Additional comment

    # Getter method to retrieve the feedback ID
    def get_feedback_id(self):
        return self._feedback_id

    # Setter method to update the feedback ID
    def set_feedback_id(self, feedback_id):
        self._feedback_id = feedback_id

    # Getter method to retrieve the guest who provid the feedback
    def get_guest(self):
        return self._guest

    # Setter method to update the guest who provide the feedback
    def set_guest(self, guest):
        self._guest = guest

    # Getter method to retrieve the rating given by the guest
    def get_rating(self):
        return self._rating

    # Setter method to update the rating given by the guest
    def set_rating(self, rating):
        self._rating = rating

    # Getter method to retrieve the comments provide by the guest
    def get_comments(self):
        return self._comments

    # Setter method to update the comments provide by the guest
    def set_comments(self, comments):
        self._comments = comments

    def __str__(self):
        # Return feedback detail
        return "Feedback ID: " + self._feedback_id + " | Guest: " + self._guest.get_name() + " | Rating: " + str(self._rating) + " | Comments: " + self._comments
