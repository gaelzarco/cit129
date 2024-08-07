make = input("Please enter the make of your vehicle:")
if make != "honda":
    print("Invalid make!")    
else:
    start_miles = float(input("Enter the starting Odometer reading:"))
    end_miles = float(input("Enter the ending Odometer reading:"))

    if end_miles < start_miles:
        print("Starting miles must be higher than ending miles!")
    else:
        gas = float(input("Enter the gallons of fuel used:"))
        gas_price = float(input("Enter the price per gallon:"))
        miles_driven = end_miles - start_miles
        miles_per_gallon = miles_driven / gas
        trip_cost = gas_price * gas

        print("\n\nCar's make:", make)
        print("Miles driven:", format(miles_driven, '.2f'))
        print("Gallons of gas used:", format(gas, '.2f'))
        print("Price per gallons of gas: $", format(gas_price, '.2f'), sep="")
        print("Miles per gallon:", format(miles_per_gallon, '.2f'))
        print("Trip fuel cost: $", format(trip_cost, '.2f'), sep="")
