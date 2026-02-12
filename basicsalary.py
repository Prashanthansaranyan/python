basicsalary=int(input("Enter your salary"))
if basicsalary>100000:
	tax=basicsalary*0.05
elif basicsalary>80000:
	tax=basicsalary*0.03
else:
	tax=0
	
print("your salary is :",basicsalary)
print("your tax is :",tax)
print("your next salary is :",(basicsalary-tax))
	
	