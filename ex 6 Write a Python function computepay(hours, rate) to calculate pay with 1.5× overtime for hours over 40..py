#Rewrite your pay computation with time-and-a-half for overtime andcreate a function called computepay which takes two parameters (hours and rate).Enter Hours: 45Enter Rate: 10Pay: 475.0
def compute_pay(hours, rate):
    if hours < 40:
        pay = hours * rate
    elif hours < 60:
        pay = (40 * rate) + (hours - 40) * rate * 1.5
    else:
        pay = 40 * rate + 20 * rate * 1.5 + (hours - 60) * rate * 2.0
    return pay

hours = int(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
pay = compute_pay(hours, rate)
print("Pay:", pay)