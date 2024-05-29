# Lesson 2: OOP Fundamentals
# 1. City Infrastructure Management System

# Vehicle class definition
class Vehicle:
    def __init__(self, registration_number, type, owner):
        self.registration_number = registration_number
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to {new_owner}")

    def __str__(self):
        return f"Vehicle({self.registration_number}, {self.type}, owned by {self.owner})"

# Event class definition
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count

    def __str__(self):
        return f"Event({self.name} on {self.date}, Participants: {self.participant_count})"

# Main function to demonstrate the functionalities
def main():
    # Demonstrate Vehicle class
    print("Vehicle Registration System")
    vehicle1 = Vehicle("ABC123", "Car", "Alice")
    vehicle2 = Vehicle("XYZ789", "Motorcycle", "Bob")
    
    # Print initial vehicle details
    print(vehicle1)
    print(vehicle2)
    
    # Update owners
    vehicle1.update_owner("Charlie")
    vehicle2.update_owner("Dave")
    
    # Print updated vehicle details
    print(vehicle1)
    print(vehicle2)
    
    # Demonstrate Event class
    print("\nEvent Management System")
    event1 = Event("Music Concert", "2024-06-01")
    event2 = Event("Tech Conference", "2024-07-15")
    
    # Add participants
    event1.add_participant()
    event1.add_participant()
    event2.add_participant()
    
    # Print participant counts
    print(f"{event1.name} has {event1.get_participant_count()} participants")
    print(f"{event2.name} has {event2.get_participant_count()} participants")

# Entry point of the script
if __name__ == "__main__":
    main()
