# class and object

class Employee:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    pass

harry = Employee("Harry","Larry",44000)
rohan = Employee("Rohan","Larry",44000)

print(harry.fname,rohan.fname)
print(rohan.salary)