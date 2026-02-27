"""S = {"maths", "science", "maths", "science"}
print(S)
print(type(S))
print(len(S))

S.add("tamil")
print(S)

S.update(["physic", "chemistry", "maths"])
print(S)

S.remove("ict")
print(S)

S.discard("ict")
print(S)

#S.pop() ethavathu oru elemant delete akum
print(S)

S.clear()
print(S)

my_sub=["tamil","english"]

S.update=(my_sub)
print(S)"""

"""marks=[75,80,83,78,78,46,75,46]
m=set(marks)
print(m)
print(type(m))"""

a = {1,2,3,4,5}
b = {3,5,6,8,9,7}

"""c = a.union(b) or c=a|b
print(c)
d=a.intersection(b)
print(d)
e=a-b
print(e)
f=b-a
print(f)
g=a.symmetric_difference(b)
g=a^b
print(g)"""
a={1,2,3}
b={1,2,3,4,5}
c={4,5,6}
d=a|b|c
print(d)
e=a&b&c
print(e)
print(a>=b)
print(b.issuperset(a))
print(a.issuperset(b))
print(b>=a)
