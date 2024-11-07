#Leap year checker (Leap years are divisible by 4 but not 100 unless also divisible by 400)

year = int(input("Write the year you want to check: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    yer = "a Leap year"
    
else:
    yer = "not a Leap year"
    
print(f"The year {year} is {yer}")