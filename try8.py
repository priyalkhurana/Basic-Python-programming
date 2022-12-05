num=int(input("Enter the number of calls:"))
bill=0
if(num<101):
    bill=num
    print(bill)
elif((num>100)and(num<201)):
    bill=100+(2*(num-100))
    print(bill)
elif((num>=200)and(num<301)):
    bill=300+(3*(num-300))
    print(bill)
elif(num>=400):
    bill=600+(4*(num-400))
    print(bill)
try:
    if(bill>=500):
        raise ValueError
except ValueError:
    print("BILL IS GREATER THAN 500.")