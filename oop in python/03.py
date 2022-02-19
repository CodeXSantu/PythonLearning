# class methods

class Employee:
    no_of_employee = 0
    increament = 1.5

    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1
    def increase(self):
        self.salary = self.salary * self.increament
    
    ## class method
    @classmethod # decorator
    def change_increament(cls,amount):
        cls.increament = amount

harry = Employee("Harry","Larry",44000)
rohan = Employee("Rohan","Larry",55000)

print(harry.salary)

Employee.change_increament(2)

print(harry.salary)
harry.increase()
print(harry.salary)