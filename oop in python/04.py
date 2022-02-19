# class methods as alternative constructor

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
    
    # class methods as alternative constructor
    @classmethod 
    def from_str(cls,emp_string):
        fname,lname,salary = emp_string.split("-")
        return cls(fname,lname,salary)

harry = Employee("Harry","Larry",44000)
mahesh = Employee.from_str("mahesh-sahu-88999")

print(mahesh.fname)