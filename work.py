username="saran"
password="sa1414"
rol="admin"
user=input("Enter the username ")
if user==username:
    p=input("Enter the password")
    if p==password:
        print("your login is success")
        R=input("Enter your role")
        if R==rol:
            print("Welcome to admin dashboard")
        else:
            print("Welcome to user dashboard")
    else:
        print("involid password! try agin")
else:
    print("involid username try agin")