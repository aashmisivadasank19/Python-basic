def simple_interest(p,r,t):
    si= (p * r * t) / 100
    return si

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter years): "))
si=simple_interest(p,r,t)
print("Simple Interest =",si)
