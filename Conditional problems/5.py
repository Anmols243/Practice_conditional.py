#Suggest an activity based on the weather(eg- sunny = Go outside for a walk, Rainy = Read a book, Snowy - Build a snowman)

Weather = input("Whats the weather outside looking like? ")
if Weather == "sunny":
    print("Go outside for a walk")
elif Weather == "rainy":
    print("Read a book")
elif Weather == "Snowy":
    print("Build a snowman")
else:
    print("Please enter a valid weather (sunny, rainy, snowy)")