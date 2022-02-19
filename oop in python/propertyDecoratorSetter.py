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
    @property
    def email(self):
        if self.fname == None:
            return 'Email not set'
        else:
            return self.fname +'.'+ self.lname + '@gmail.com'

    @email.setter
    def email(self,given_email):
        
        name_list = given_email.split('@')[0].split('.')
        print(name_list)
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

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


if __name__ == '__main__':
    harry = Employee("Harry","jackson",88000)
    rohan = Employee("Rohan","agarwal",9)
    print(harry.email,rohan.email)
    rohan.lname = "Khanna"
    print(rohan.email)
    rohan.email = 'Khanna.rohan@gmail.com'
    print(rohan.email)
    del rohan.email
    print(rohan.email)