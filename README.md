# Airfare Calculator ✈️

This project calculates airfare costs based on destination, airline, and passenger details.  
It includes both the **original assignment code** and a **refactored version** to demonstrate improvement.

## Features
- Choose between Hawaii, Bahamas, or Cancun
- Select airline: US Air, Delta, United
- Handles adult and child ticket pricing
- Input validation for passenger counts
- Refactored version with cleaner functions and reusable logic

## Project Structure
AirfareCalculator/ 
│── older version/ # Original assignment code 
│── older version 2/ # extended assignment code 
│── refactored/ # Improved, function-based design


## Usage
Run the refactored version:
```bash
python refactored_version/airfare_refactored.py

Example
Vacation destination (Hawaii or Bahamas): Hawaii
Number of passengers (1–3): 2
Number of passengers under 18: 1
Airline (US Air or Delta): US Air

--- Trip Summary ---
Destination: Hawaii
Airline: US Air
Passengers: 2 (Adults: 1, Children: 1)
Total Fare: $1950
