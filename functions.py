"""//default function
def printMyName():
	print("My name is saran")

printMyName()
printMyName()
printMyName()
//parameter
def printMyName(name):
	print(f"My name is {name}")

printMyName("a")
printMyName("b")
printMyName("c")"""


"""def printMyName(fname,lname):
	print(f"My name is {fname}{lname}")

printMyName("saran","yan")"""
"""default parameter"""
"""def printMyName(fname="saran",lname="yan"):
	print(f"My name is {fname}{lname}")

printMyName("saran","yan")
printMyName()"""

"""Return function """
def printMyName(fname,lname):
    return fname+lname
fullname=printMyName("saran","yan")
print("my name is ",fullname)