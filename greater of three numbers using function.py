def greatest_of_three(a,b,c):
    n=a;
    if (b>n):
        n=b;
    if (c>n):
        n=c;
    return (n)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
   
n = greatest_of_three(a,b,c)
print("greatest of three",n)