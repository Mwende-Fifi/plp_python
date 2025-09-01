class Vehicle:
    def move(self):
        pass  # placeholder


class Car(Vehicle):
    def move(self):
        return "Car is driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Plane is flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Boat is sailing 🚤"

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
