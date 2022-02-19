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


class Programmer(Employee):
    def __init__(self, fname, lname, salary,proglang,expr):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.expr = expr

    def increase(self):
        self.salary = self.salary * (self.increament + 0.3)

niraj = Programmer("Niraj","Pandey",70000,"c",2)

print(niraj.fname)
niraj.increase()

print(niraj.salary)

print(niraj.increase())

print(niraj.proglang,niraj.expr)

# print(help(Programmer))