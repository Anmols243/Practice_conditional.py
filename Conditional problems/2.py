# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discont on wednesday


age = int(input("How old are you? "))

day = input("Whats the day today? ")


price = 12 if age >= 18 else 8

if day == "Wednesday":
    print("Price: ", price - 2)

else:
    print("Price:", price)

    