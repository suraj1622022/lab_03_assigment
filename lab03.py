class Flight:
    def __init__(self, flight_id, origin, destination, price):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
        
    def add_flight(self, flight):
        self.flights.append(flight)
        
    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.origin == city or flight.destination == city:
                result.append(flight)
        return result
        
    def search_by_origin(self, origin):
        result = []
        for flight in self.flights:
            if flight.origin == origin:
                result.append(flight)
        return result
        
    def search_between_cities(self, city1, city2):
        result = []
        for flight in self.flights:
            if (flight.origin == city1 and flight.destination == city2) or \
               (flight.origin == city2 and flight.destination == city1):
                result.append(flight)
        return result
        
def print_flights(flights):
    if not flights:
        print("No flights found.")
    else:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in flights:
            print(f"{flight.flight_id}\t{flight.origin}\t{flight.destination}\t{flight.price}")

# Creating Flight objects
flights_data = [
    ("AI161E90", "BLR", "BOM", 5600),
    ("BR161F91", "BOM", "BBI", 6750),
    ("AI161F99", "BBI", "BLR", 8210),
    ("VS171E20", "JLR", "BBI", 5500),
    ("AS171G30", "HYD", "JLR", 4400),
    ("AI131F49", "HYD", "BOM", 3499)
]

flight_table = FlightTable()

for data in flights_data:
    flight = Flight(*data)
    flight_table.add_flight(flight)

# Main program
while True:
    print("\nMenu:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        city = input("Enter city: ")
        flights = flight_table.search_by_city(city)
        print_flights(flights)
    elif choice == "2":
        origin = input("Enter origin city: ")
        flights = flight_table.search_by_origin(origin)
        print_flights(flights)
    elif choice == "3":
        city1 = input("Enter first city: ")
        city2 = input("Enter second city: ")
        flights = flight_table.search_between_cities(city1, city2)
        print_flights(flights)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
