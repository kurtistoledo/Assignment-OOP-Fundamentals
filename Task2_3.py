# Lesson 2: OOP Fundamentals
# 3. City Services Simulation: Python OOP and Modular Design

# transportation.py

class Bus:
    # Class variables
    city_name = "Metropolis"
    base_fare = 2.50
    
    def __init__(self, route_number, passenger_capacity):
        # Instance variables
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity

    def __str__(self):
        return (f"Bus(Route Number: {self.route_number}, "
                f"Passenger Capacity: {self.passenger_capacity}, "
                f"City: {Bus.city_name}, Base Fare: ${Bus.base_fare:.2f})")

    @classmethod
    def update_base_fare(cls, new_fare):
        cls.base_fare = new_fare

# main.py
from Task2_3 import Bus

def main():
    # Create instances of Bus
    bus1 = Bus(101, 50)
    bus2 = Bus(202, 75)
    
    # Print initial bus details
    print("Initial Bus Details:")
    print(bus1)
    print(bus2)
    
    # Update base fare using class method
    Bus.update_base_fare(3.00)
    
    # Print updated bus details
    print("\nUpdated Bus Details after changing base fare:")
    print(bus1)
    print(bus2)

    # Access class variables from instances
    print("\nAccessing class variables from instances:")
    print(f"Bus1 City: {bus1.city_name}, Base Fare: ${bus1.base_fare:.2f}")
    print(f"Bus2 City: {bus2.city_name}, Base Fare: ${bus2.base_fare:.2f}")

if __name__ == "__main__":
    main()
