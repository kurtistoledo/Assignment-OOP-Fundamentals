# Lesson 2: OOP Fundamentals
# 2. Python City Planning Simulator

import json

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def save_to_file(self, filename):
        building_data = {
            "name": self.name,
            "floors": self.floors
        }
        with open(filename, 'a') as file:
            file.write(json.dumps(building_data) + "\n")

    @classmethod
    def load_from_file(cls, filename):
        buildings = []
        with open(filename, 'r') as file:
            for line in file:
                building_data = json.loads(line.strip())
                building = cls(building_data["name"], building_data["floors"])
                buildings.append(building)
        return buildings

    def __str__(self):
        return f"Building(Name: {self.name}, Floors: {self.floors})"

def main():
    # Create instances of Building
    building1 = Building("Empire State Building", 102)
    building2 = Building("Burj Khalifa", 163)
    
    # Save buildings to file
    building1.save_to_file("buildings.txt")
    building2.save_to_file("buildings.txt")
    
    # Load buildings from file
    buildings = Building.load_from_file("buildings.txt")
    
    # Print loaded buildings
    for building in buildings:
        print(building)

if __name__ == "__main__":
    main()
