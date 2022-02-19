# while condition == True 

x = [3,4,42,2,4,6]

i = 0
while i < len(x):
    print(x[i])
    i = i + 1



i = 0
while i < 10:
    print("run")
    i += 1

    # or 
    
i = 0
while True:
    print("run")
    i += 1
    if i == 10:
        break