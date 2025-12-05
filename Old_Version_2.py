#!/usr/bin/env python
# coding: utf-8

# In[5]:


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
import sys


HawaiiAirFare = 200
BahamasAirFare = 400
CancunAirFare = 600
usAdultAirTicket = 1000
deltaAdultTicket = 1200
cancunAdultTicket = 1500
usAirChildTicket = 750
deltaChildTicket = 900
cancunChildTicket = 1125


def calculation(placeofVacation, airlineChoice, numOfPassenger, numofUnderagePass):
#adding airfare
    if placeofVacation == "Hawaii":
        print("Hawaii Air Fare: $", HawaiiAirFare)
        totalAirFare = HawaiiAirFare
    elif placeofVacation == "Bahamas":
        print("Bahamas Air Fare: $", BahamasAirFare)
        totalAirFare = BahamasAirFare
    elif placeofVacation == "Cancun":
        print("Cancun Air Fare: $", CancunAirFare)
        totalAirFare = CancunAirFare
#Loop to check for airline choice
    if airlineChoice == "US Air":
        print("Adult ticket price: $", usAdultAirTicket)
        totalAdult = (numOfPassenger - numofUnderagePass) * usAdultAirTicket
        print("Total Adult ticket price: $", totalAdult)
#calculating total air fare
        totalAirFare = totalAirFare + totalAdult
#loop to check for underage passenger
        if numofUnderagePass != 0 and not(numofUnderagePass >= numOfPassenger):
        #calculating final total air fare
            print("Child ticket price: $", usAirChildTicket)
            totalChild = numofUnderagePass * usAirChildTicket
            print("Total child ticket price $: ", totalChild)
            totalAirFare = totalAirFare + totalChild
            print("Total air fares: $", totalAirFare)
        elif numofUnderagePass == 0:
            print("Total air fares: $", totalAirFare)
    elif airlineChoice == "Delta":
        print("Adult ticket price: $", deltaAdultTicket)
        totalAdult = (numOfPassenger - numofUnderagePass) * deltaAdultTicket
        print("Total Adult ticket price: $", totalAdult)
#calculating total air fare
        totalAirFare = totalAirFare + totalAdult
#loop to check for underage passenger
        if numofUnderagePass != 0 and not(numofUnderagePass >= numOfPassenger):
    #calculating final total air fare
            print("Child ticket price: $", deltaChildTicket)
            totalChild = numofUnderagePass * deltaChildTicket
            print("Total child ticket price $: ", totalChild)
            totalAirFare = totalAirFare + totalChild
            print("Total air fares: $", totalAirFare)
        elif numofUnderagePass == 0:
            print("Total air fares: $", totalAirFare)
    elif airlineChoice == "Cancun":
        print("Adult ticket price: $", cancunAdultTicket)
        totalAdult = (numOfPassenger - numofUnderagePass) * cancunAdultTicket
        print("Total Adult ticket price: $", totalAdult)
#calculating total air fare
        totalAirFare = totalAirFare + totalAdult
#loop to check for underage passenger
        if numofUnderagePass != 0 and not(numofUnderagePass >= numOfPassenger):
    #calculating final total air fare
            print("Child ticket price: $", cancunChildTicket)
            totalChild = numofUnderagePass * cancunChildTicket
            print("Total child ticket price $: ", totalChild)
            totalAirFare = totalAirFare + totalChild
            print("Total air fares: $", totalAirFare)
        elif numofUnderagePass == 0:
            print("Total air fares: $", totalAirFare)
            
            
def passenger(placeofVacation, airlineChoice):
    numOfPassenger = int(input("Please enter the number of people aboarding the plane: "))
    numofUnderagePass = int(input("How many passenger(s) will be under the age of 18? "))
 #loop to check for underage passenger  
    if numofUnderagePass != 0 and not(numofUnderagePass >= numOfPassenger):
        print("/**********/")
        print("Number of passenger(s): ", numOfPassenger)
        print("Number of passenger(s) under the age of 18: ", numofUnderagePass)
        print("/**********/")
        calculation(placeofVacation, airlineChoice, numOfPassenger, numofUnderagePass)
    elif numofUnderagePass == 0:
        print("/**********/")
        print("Number of passenger(s): ", numOfPassenger)
        print("/**********/")
        calculation(placeofVacation, airlineChoice, numOfPassenger, numofUnderagePass)
    else:
        print("/**********/")
        print("Please enter the correct number of underage of passenger, cannot be equal to or exceed total passengers for safety concerns")
        sys.exit()    

def carrier(placeofVacation):
    airlineChoice = str(input("Please select an airline: US Air, Delta, United: "))
#Loop to check for airline choice
    if airlineChoice == "US Air":
        print("/**********/")
        print("Airline choice: US Air")
        passenger(placeofVacation, airlineChoice)
    elif airlineChoice == "Delta":
        print("/**********/")
        print("Airline choice: Delta")
        passenger(placeofVacation, airlineChoice)
    elif airlineChoice == "United":
        print("/**********/")
        print("Airline choice: United")
        passenger(placeofVacation, airlineChoice)
    else:
        print("/**********/")
        print("Invalid option, please select one of the two airline options!")
        sys.exit()
        
        
def main():
    placeofVacation = str(input("Please select a place to visit; Hawaii, Bahamas, or Cancun: "))

    #Loop to check which location is chosen or return error when chosen an invalid option
    if placeofVacation == "Hawaii":
        print("/**********/")
        print("Place of Vacation: Hawaii")
        carrier(placeofVacation)
    elif placeofVacation == "Bahamas":
        print("/**********/")
        print("Place of Vacation: Bahamas")
        carrier(placeofVacation)
    elif placeofVacation == "Cancun":
        print("/**********/")
        print("Place of Vacation: Cancun")
        carrier(placeofVacation)
    else:
        print("/**********/")
        print("Invalid place, please select one of the three option!")
        sys.exit()
main()


# In[ ]:




