#Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
largest = int(input("Enter first number: "))
smallest = largest

for i in range(4):
    num = int(input("Enter a number: "))

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Maximum =", largest)
print("Minimum =", smallest)