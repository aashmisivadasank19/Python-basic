percentage=float(input("Enter your 12th percentage: "))
physics=input("Did you have physics in 12th? (yes/no): ").lower()
mathematics=input("Did you have mathematics in 12th? (yes/no): ").lower()
if percentage >= 75 and physics == "yes" and mathematics == "yes":
    print("You are eligible for the course.")
else:
    print("You are not eligible for the course.")