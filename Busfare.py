class Vehicle:
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
        return self.capacity * 100 * 1.10
bus = Bus()
bus.capacity = 50
print("Total Bus Fare: INR", bus.fare())