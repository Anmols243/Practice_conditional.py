#Choose a mode of transportation based on the distance(eg <3km: Walk, 3-15km: bike, >15km: car)

try:
    distance = float(input("Whats the distance of the location? "))

    if 0 < distance < 3:
        print("Walk")
    elif 3 < distance < 15:
        print("Bike")
    elif distance > 15:
        print("Car")

except ValueError:
    print("Please enter valid information")