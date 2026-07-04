total = 0
n = int(input("How many numbers do you want to add? "))

for i in range(n):
    num = int(input("Enter a number: "))
    total += num

print("Sum =", total)