#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""PSEUDOCODE

BahamasAirFare = 300
HawaiiAirFare = 200
usAdultAirTicket = 1000
deltaAdultTicket = 1200
usAirChildTicket = 750
deltaChildTicket = 900


placeofVacation = str(input("Please select a place to visit: Hawaii or Bahamas \n")
numOfPassenger = int(input("Please enter the number of people, up to 3 and cannot be 0 \n")
numofUnderagePass = int(input("How many passenger(s) will be under the age of 18?  \n")
airlineChoice = str(input("Please select an airline: US Air or Delta \n")

If place = Hawaii
	Print Hawaii
	totalAirFare = HawaiiAirFare
Else place =Bahamas
	Print Bahamas
	totalAirFare = BahamasAirFare


//Loop to check for airline choice
If airlineChoice = US Air
	Print US air
	Print usAdultAirTicket
	totalAirFare = numOfPassenger * usAdultAirTicket
//Loop to check for underage 
If numofUnderagePass != 0 and numofUnderagePass < numOfPassenger
			totalAirFare = totalAirFare + (numofUnderagePass * usAirChildTicket)
			Display usAirChildTicket
	`		Display totalAirFare
		Else 
			Display USAirChildTicket
			Display totalAirFare
Else airlineChoice = Delta
	Print Delta
	Print deltaAirTicket
	totalAirFare = numOfPassenger * usAdultAirTicket
If numofUnderagePass != 0
			totalAirFare = totalAirFare + (numofUnderagePass * deltaChildTicket)
			Display deltaChildTicket
			Display totalAirFare
		Else 
			Display deltaChildTicket
			Display totalAirFare
"""

#Defining prices
HawaiiAirFare = 200
BahamasAirFare = 400
usAdultAirTicket = 1000
deltaAdultTicket = 1200
usAirChildTicket = 750
deltaChildTicket = 900

#Asking inputs
placeofVacation = str(input("Please select a place to visit, Hawaii or Bahamas: "))
numOfPassenger = int(input("Please enter the number of people aboarding the plane: "))
numofUnderagePass = int(input("How many passenger(s) will be under the age of 18? "))
airlineChoice = str(input("Please select an airline: US Air or Delta: "))

#Loop to check which location is chosen or return error when chosen an invalid option
if placeofVacation == "Hawaii":
    print("/**********/")
    print("/**********/")
    print("Place of Vacation: Hawaii")
    print("Hawaii Air Fare: $", HawaiiAirFare)
    totalAirFare = HawaiiAirFare
elif placeofVacation == "Bahamas":
    print("/**********/")
    print("/**********/")
    print("Place of Vacation: Bahamas")
    print("Hawaii Air Fare: $", BahamasAirFare)
    totalAirFare = BahamasAirFare
else:
    print("/**********/")
    print("Invalid place, please select one of the two option!")
    sys.exit()

#Loop to check for airline choice
if airlineChoice == "US Air":
    print("Airline choice: US Air")
    print("Adult ticket price: $", usAdultAirTicket)
#calculating total air fare
    totalAirFare = totalAirFare + ((numOfPassenger - numofUnderagePass) * usAdultAirTicket)
#loop to check for underage passenger
    if numofUnderagePass != 0 and not(numofUnderagePass >= numOfPassenger):
        #calculating final total air fare
        totalAirFare = totalAirFare + (numofUnderagePass * usAirChildTicket)
        print("Child ticket price: $", usAirChildTicket)
        print("Total air fares: $", totalAirFare)
    elif numofUnderagePass == 0:
        print("Child ticket price: $", usAirChildTicket)
        print("Total air fares: $", totalAirFare)
    else:
        print("/**********/")
        print("Please enter the correct number of underage of passenger, cannot be equal to or exceed total passengers for safety concerns")
        sys.exit()
else: 
    if airlineChoice == "Delta":
        print("Airline choice: Delta")
        print("Adult ticket price: $", deltaAdultTicket)
        totalAirFare = totalAirFare + (numOfPassenger - numofUnderagePass) * deltaAdultTicket
    
        if numofUnderagePass != 0 and not(numofUnderagePass >= numOfPassenger):
            totalAirFare = totalAirFare + (numofUnderagePass * deltaChildTicket)
            print("Child ticket price: $", deltaChildTicket)
            print("Total air fares: $", totalAirFare)
        elif numofUnderagePass == 0:
            print("Child ticket price: $", deltaChildTicket)
            print("Total air fares: $", totalAirFare)
        else:
            print("/**********/")
            print("Please enter the correct number of underage of passenger, cannot be equal to or exceed total passengers!")
            sys.exit()
    else: 
        print("/**********/")
        print("Invalid option, please select one of the two airline options!")
        sys.exit()


# In[ ]:




