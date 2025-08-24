try:
    percentage = float(input("Enter your percentage: "))
    if percentage > 100:
        print("Percentage cannot be greater than 100.")
    elif percentage >= 90:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    elif percentage >=50:
        print("Grade: E")
    else:
        print("Grade: F")
except ValueError:
    print("Please enter a valid number.")
