import sys

# Ticket prices stored in dictionaries
AIRFARES = {
    "Hawaii": 200,
    "Bahamas": 400
}

TICKET_PRICES = {
    "US Air": {"adult": 1000, "child": 750},
    "Delta": {"adult": 1200, "child": 900}
}

def validate_inputs(place, airline, num_passengers, num_underage):
    if place not in AIRFARES:
        print("Invalid place. Choose Hawaii or Bahamas.")
        sys.exit()
    if airline not in TICKET_PRICES:
        print("Invalid airline. Choose US Air or Delta.")
        sys.exit()
    if num_passengers <= 0 or num_passengers > 3:
        print("Invalid number of passengers. Must be between 1 and 3.")
        sys.exit()
    if num_underage < 0 or num_underage >= num_passengers:
        print("Invalid number of underage passengers.")
        sys.exit()

def calculate_fare(place, airline, num_passengers, num_underage):
    # Base fare for destination
    total = AIRFARES[place]
    
    # Adult tickets
    adult_count = num_passengers - num_underage
    total += adult_count * TICKET_PRICES[airline]["adult"]
    
    # Child tickets
    total += num_underage * TICKET_PRICES[airline]["child"]
    
    return total

def main():
    # Inputs
    place = input("Vacation destination (Hawaii or Bahamas): ").strip()
    num_passengers = int(input("Number of passengers (1–3): "))
    num_underage = int(input("Number of passengers under 18: "))
    airline = input("Airline (US Air or Delta): ").strip()
    
    # Validate
    validate_inputs(place, airline, num_passengers, num_underage)
    
    # Calculate
    total_fare = calculate_fare(place, airline, num_passengers, num_underage)
    
    # Output
    print("\n--- Trip Summary ---")
    print(f"Destination: {place}")
    print(f"Airline: {airline}")
    print(f"Passengers: {num_passengers} (Adults: {num_passengers - num_underage}, Children: {num_underage})")
    print(f"Total Fare: ${total_fare}")

if __name__ == "__main__":
    main()
