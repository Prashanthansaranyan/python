day=int(input("Enter your day : "))
match day:
    case 1:
        print("today is monday")
    case 2:
        print("today is tuesday")
    case 3:
        print("today is wednesday")
    case 4:
        print("today is thuesday")
    case 5:
        print("today is friday")
    case 6:
        print("today is saturday")
    case 7:
        print("today is sunday")
    case _:
        print("invalid")