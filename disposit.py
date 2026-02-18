print("Well come to yit bank")
n=input("Enter your name : ")
i=int(input("Enter your NIC number : "))
s=int(input("Enter your disposit amount : "))
t=int(input("How meny month you disposit"))
r=3

def printdis1():
	A=s*(r//100)
	print(s+A)
def printdis2():
	A=s*(r//100)*(3//12)
	print(s+A)
def printdis3():
	A=s*(r//100)*(6//12)
	print(s+A)
def printdis4():
	A=s*(r//100)*(12//12)
	print(s+A)
def printdis5():
	A=s*(1+r//100)*(18//12)
	print(s+A)
def printdis6():
	A=s*(r//100)*(24//12)
	print(s+A)
	
match t:
        case 1:
            printdis1()  
        case 3:
          printdis2() 
        case 6:
          printdis3() 
        case 12:
          printdis4() 
        case 18:
          printdis5() 
        case 24:
          printdis6() 
        case _:
          print(" in valid") 