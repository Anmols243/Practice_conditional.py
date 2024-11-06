#Customize a coffee order: small, medium or large with an option for extra shot of espresso

name = input("Whats your name? ").upper()
order_size = None
extra_shot = None

while order_size not in["large", "medium", "small"]:
    order_size = input("What size would you like to order? ").lower()
    if order_size not in ["large" , "medium", "small"]:
        print("Please give a valid input or e to exit")
    elif extra_shot =="e":
        break

while extra_shot not in["yes", "no"]:
    extra_shot = input("Would like an extra shot? ").lower()
    if extra_shot not in ["yes" or "no"]:
        print("Please give a valid input or e to exit")
    elif extra_shot == "e":
        break   

if extra_shot == "yes":
    coffee = order_size + f" coffee with an extra shot for {name}"
else:
    coffee = order_size + f" coffe for {name}"

print(coffee)