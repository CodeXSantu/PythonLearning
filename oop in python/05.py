# Static function -- method which do not take class and instance 
# variable as argument

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



# subham = Employee('Subham',"Mohan",70000)
print(Employee.is_open('sunday'))
print(Employee.is_open('monday'))