# class variable and instance variable

class Employee:
    no_of_employee = 0
    increament = 1.5  # class variable for every object created from this class
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1
    pass
    def increase(self):
        self.salary = self.salary * self.increament  # first check instance variable then class variable
        #self.salary = self.salary * Employee.increament # direct go to class variable

harry = Employee("Harry","Larry",44000)
rohan = Employee("Rohan","Larry",44000)

print(harry.salary)
harry.increase()
print(int(harry.salary))
harry.increament = 9

# show all variable of instance
print(harry.__dict__)
#show all variable of class
print(Employee.__dict__)

print(Employee.no_of_employee)