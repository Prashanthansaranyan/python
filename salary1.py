salaries = [50000, 100000, 300000, 500000,1000000,200000,2010000]

i = 0

while i < len(salaries):
    salary = salaries[i]
    
    if salary <= 50000:
        tax = salary * 0.03
        
    elif salary <= 100000:
        tax = (50000 * 0.03) + ((salary - 50000) * 0.05)
        
    elif salary <= 300000:
        tax = (50000 * 0.03) + (50000 * 0.05) + ((salary - 100000) * 0.08)
        
    else:
        tax = (50000 * 0.03) + (50000 * 0.05) + (200000 * 0.08) + ((salary - 300000) * 0.10)
    
    print(salary - tax)
    
    i += 1