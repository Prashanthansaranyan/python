day1="monday"
day2="tuesday"
day3="wednesday"
day4="thursday"
day5="friday"
day6="saturday"
day7="sunday"
day=int(input("which day you want : "))
if 0<day<=7:
    if day==1:
        print("today is : ",day1)
    elif day==2:
        print("today is : ",day2)
    elif day==3:
        print("today is : ",day3)
    elif day==4:
        print("today is : ",day4)
    elif day==5:
        print("today is : ",day5)
    elif day==6:
        print("today is : ",day6)
    else:
        print("today is : ",day7)
else:
    print("invalid!")
