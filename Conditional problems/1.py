#classify a person's age group: child (<13), Teenager(13-19), Adult(20-59), Senior(60+)

age_input = int(input("Please write your age: "))

try:
    if age_input < 13:
        print("You are a child")
    elif 13 < age_input < 19:
        print("You are a Teenager")
    elif 20 < age_input < 59:
        print("You are an Adult")
    elif age_input > 60:
        print("You are a Senior")

except ValueError:
    print("Please enter a valid input")
