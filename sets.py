# set is unodered unique data collection 


z = {4,45,34,4,5,3,2}
y = {} # if empty create dictionaries
x = set() # so this method is best for creating set


print(type(y),":",type(z))


z.add(4)
z.remove(5)

print(z)

print(4 in z)

print(1 in z)


s1 = {4,32,4,22}
s2 = {2,4,634,4,2}
print(s1.union(s2))
print(s1.difference(s2))
print(s1.intersection(s2))