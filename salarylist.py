salaries = [50000,100000,300000,500000]
i=0
while i<= len(salaries):
    salary=salaries[i]
    if salary <= 50000:
        tax =salary*0.03
    elif salary <= 100000:
        tax = (salary) - 50000) * 0.05+(salary)*0.03
        print((salary)-tax)
    elif (salary)<=300000 :
        tax =(salary)-100000)*0.08+(salary) - 50000) * 0.05+(salary)*0.03
        print((salaries[i])-tax)
    else:
        tax=((salary)-300000)*0.1+((salary) - 50000) * 0.05+(salary)*0.03+(salaries[i]-100000)*0.08
        print(salary)-tax)

        