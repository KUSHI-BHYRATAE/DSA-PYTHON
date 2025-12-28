# Simple Traffic Light Simulator

color = input("Enter traffic light color (red/yellow/green): ").lower()

if color == "red":
    print("STOP!")
elif color == "yellow":
    print("Prepare to stop")
elif color == "green":
    print("You can go")
else:
    print("Wrong input!")
