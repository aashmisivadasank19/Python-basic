

while True:
    num = input("Enter a number: ")
    largest = None
    smallest = None
    if num == "done":
        break

    n = int(num)

    if largest is None or n > largest:
        largest = n

    if smallest is None or n < smallest:
        smallest = n

print("Maximum =", largest)
print("Minimum =", smallest)