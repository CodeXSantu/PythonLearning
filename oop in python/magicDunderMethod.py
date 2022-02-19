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

        
    # static method
    @staticmethod
    def is_open(day):
        if day == 'sunday':
            return False
        else:
            return True

    # Dunder or magic method
    def __add__(self,other):
        return  self.salary + other.salary

    def __repr__(self):
        return f"Employee({self.fname},{self.lname},{self.salary})"

    def __str__(self): #override __repr__()
        return f'The name of employee is {self.fname}'
niraj = Employee("Niraj","Pandey",70000)
rohan = Employee("Rohan","Pandey",7000)

print(niraj.fname)

print(niraj + rohan)
print(repr(niraj))
print(str(niraj))

#Dunder method

# a = 6 

# print(a.__add__(7))
# print(a.__mul__(7))