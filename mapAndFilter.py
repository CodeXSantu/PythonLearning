x = [1,2,3,4,6,7,7,3,6,4,8,456,114,132]

mp = map(lambda i : i + 2,x)
print(list(mp))


fl = filter(lambda i: i %2 == 0,x)
print(list(fl))