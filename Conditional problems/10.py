#Pet food recommendation, recommend a type of pet food based on the pet's species and age. (Dog:<2 years - puppy food, cat: >5 years - senior cat food)

valid_pets = ["dog" , "cat"]

pet = input("What pet do you have? ").lower()

if pet not in valid_pets:
    print(f"Sorry, we dont provide food recommendations for {pet}")

else:
    try:
        age = int(input(f"Whats the age of your {pet}? "))

        food = None
        if pet == "dog":
            food = "Puppy food" if age <= 2 else "Senior dog food"

        elif pet == "cat":
            food = "Kitten food" if age <= 5 else "Senior cat food"
        
        if food:
            print(f"We recommend {food} for your {pet} of age {age}")

    except ValueError:
        print("Please provide a valid number for age input")





