x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2

#chaining condition 

# and  ---- precedence rule (not,and or)
# or 
# not

result4 = result1 and result3

result5 = result4 or result2 and result2
result6 = not result1

print(result4)
print(result5)
print(result6)