# : Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers
total = 0
count = 0

while True:
    n = input("Enter a number: ")

    if n == "done":
        break

    num = int(n)
    total = total + num
    count = count + 1
    average = total / count

print("Total =", total)
print("Count =", count)
print("Average =", average)