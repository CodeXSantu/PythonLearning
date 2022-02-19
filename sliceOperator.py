x = [0,1,2,3,4,5,6,7,8,9]

y = ('hi','hello','goodbye','cya','sure')

s = 'hello'


sliced1 =   x[0:4:2]                                 #[start:stop:step]
sliced2 =   y[4:0:-1]                                 #[start:stop:step]

print(sliced1)
print(sliced2)

# reversed list 

reverse = x[::-1]
print(reverse)

reverse1 = y[::-1]
print(reverse1)