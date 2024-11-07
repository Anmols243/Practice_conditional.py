#password strength checker(Check if passowrd is: weak, medium or strong, criteria: <6 chars(weak),6-10 chars(medium),>10 (strong))

pswrd = input("Please enter a password: ")

try:
   int(pswrd)
   print("Please use characters not just numbers")
except ValueError:
    length = len(pswrd)
    strength = None
      
    if length < 6:
        strength = "Weak"

    elif 6 <= length < 10:
        strength = "Medium"

    elif length >= 10:
        strength = "Strong"

    print(f"Your password is {strength}")