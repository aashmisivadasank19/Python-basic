a= int(input("Enter year:"))
b=a%4
if(b==0):
    print("The year is leap year")
elif(b!=0):
    print("The year is not leap year")   
else:
    print("INVALID")