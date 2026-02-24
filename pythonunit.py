unit=int(input("Enter your unit"))
if 0<unit<90:
    bill=unit*7
    print(bill)
elif unit<150:
    bill1=((unit-90)*10)+(90*7)
    print(bill1)
elif unit<300:
    bill2=((unit-150)*15)+(90*7)+(60*10)
    print(bill2)
else:
    bill6=((90*7+60*10+150*15)*0.03)
    print((90*7+60*10+150*15)+bill6)