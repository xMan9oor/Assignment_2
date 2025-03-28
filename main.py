
# main.py
# This file runs the Royal Stay Hotel Management System
# It imports the test cases from test_cases.py and executes them

# Import all test functions from test_cases module
import test_cases

def main():
    # Run every test case
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* Guest Account Creation Test *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    test_cases.test_guest_account_creation()
    print()
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* Search Available Rooms Test *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    test_cases.test_search_available_rooms()
    print()
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* Room Reservation Test *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    test_cases.test_room_reservation()
    print()
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* Booking Confirmation Notification Test *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    test_cases.test_booking_confirmation_notification()
    print()
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* Invoice Generation Test *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    test_cases.test_invoice_generation()
    print()
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* Payment Processing Test *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    test_cases.test_payment_processing()
    print()
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* Reservation History Test *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    test_cases.test_reservation_history()
    print()
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* Cancellation of Reservation Test *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    test_cases.test_cancellation_reservation()

if __name__ == "__main__":
    main()
