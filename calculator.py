num1=int(input("Enter the number1 : "))
num2=int(input("Enter the number2 : "))
print( " What is you want ")
print("Addition Enter the number 1")
print("Subtraction Enter the number 2")
print("Multiplication Enter the number 3")
print("Division Enter the number 4")
num=int(input("Enter the number"))
print("----------------------------")
print("Your first number is : ",num1)
print("Your scend number is : ",num2)
match num:
	case 1:
		sum=num1+num2
		print("your total : ",sum)
	case 2:
		sum=num1-num2
		print("your total : ",sum)
	case 3:
		sum=num1*num2
		print("your total : ",sum)
	case 4:
		sum=num1/num2
		print("your total : ",sum)
	case _:
		print("invalid")
