#Assign a letter grade based on a student's score: A(90-100),B(80-89),C(70-79),D(60-69),F(below 60)

try:
    score = float(input("What's your score? "))
    if score < 0:
        raise ValueError("Negative value")
    elif 90 <= score <= 100:
        print("A")
    elif 80 <= score < 90:
        print("B")
    elif 70 <= score < 80:
        print("C")
    elif 60 <= score < 70:
        print("D")
    elif score < 60:
        print("F")
except ValueError:
    print("Please enter a valid score")
