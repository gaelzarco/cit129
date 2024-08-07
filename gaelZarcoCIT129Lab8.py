def getNumTemps():
    numReadings = int(input("Please enter the amount of temperature readings to perform: ")) 

    while numReadings > 10 or numReadings < 1:
        numReadings = int(input("Error. The amount of temperature readings must be between 1 and 10: "))

    return numReadings

def getData(numReadings, temps):
    for r in range(numReadings):
        curr = int(input(f"Please enter the temperature value for reading {r + 1}: "))

        temps.append(curr)

def displayMessage(numReadings, temps):
    avgTemp = (sum(temps)) / numReadings
    displayMessage = ""

    if avgTemp < 20:
        displayMessage = "Cold"
    elif avgTemp >= 20 and avgTemp <=35:
        displayMessage = "Okay"
    elif avgTemp > 35:
        displayMessage = "Hot"

    print(f"\nAverage Temperature: {avgTemp}")
    print(f"Message: {displayMessage}")

def displayData(numReadings, temps):
    print("\nSUMMARY Temperature DATA")

    for r in range(numReadings):
        print(f"{temps[r]}")


def main():
    numReadings = getNumTemps()
    temps = []
    getData(numReadings, temps)
    displayMessage(numReadings, temps)
    displayData(numReadings, temps)

if __name__ == "__main__":
    main()
    
