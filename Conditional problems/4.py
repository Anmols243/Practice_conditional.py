#Determine if a fruit is ripe, overripe, or unripe based on its color(Green,Yellow,Brown), eg-banana

fruit = input("Which fruit do you want to check? ")

if fruit == "Banana":

    color = input("whats the color of the fruit? ")

    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overipe")
    else:
        print(f"Are you sure {color} is the right color?")
else:
    print(f"I am sorry {fruit} isnt available in our directory yet")


