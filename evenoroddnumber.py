num=int(input("Enter the number "))
print("your number is :",num)
num2=num%2
if num>=0:
    print(num2)
    if num2 ==0:
        print("this number is even number")
    else:
        print("this number is odd number")
else :
        print("your number is involid")
