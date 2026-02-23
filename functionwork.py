num1=int(input("Enter your number1"))
num2=int(input("Enter your number2"))
num=int(input("Enter the number"))
def	printAddition():
	sum=num1+num2
	print("your total : ",sum)
def	printSubtraction():
	sum=num1-num2
	print("your total : ",sum)
def	printMultiplication():
	sum=num1*num2
	print("your total : ",sum)
def	printDivision():
	sum=num1/num2
	print("your total : ",sum)
		
match num:
        case 1:
          printAddition()  
        case 1:
          printSubtraction() 
        case 1:
          printMultiplication() 
        case 1:
          printDivision() 
        case _:
          print(" in valid") 