# class and objects

class Employee:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    pass


harry = Employee()
rohan = Employee()


harry.fname = 'Harry'
harry.lname = "Larry"
harry.salary = 44000

rohan.fname = "Rohan"
rohan.lname = "Larry"
rohan.salary = 44000

print(harry.salary)
print(harry.fname)

print(harry,rohan)