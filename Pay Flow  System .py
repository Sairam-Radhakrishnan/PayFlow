

print("                             💵 PayFlow - Employee Payroll System                  ")

class employee():
    def __init__(self,id, name,hire_date,shift,dob,age,pay,type_job):
        self._id = id
        self.name = name
        self.hire_date = hire_date
        self.shift = shift
        self.__dob = dob
        self.__age = age
        self.pay = pay
        self.type_job = type_job

    def display_full_report(self):
        print("           Employee Report       ")
        print("--------------------------------")
        print("Name of Employee : ",self.name)
        print("Employee ID      : ",self._id)
        print("Shift            : ",self.shift)
        print("Date of Birth    :",self.__dob)
        print("Age              :",self.__age)
        print("CTC              : ₹ ",self.pay)
        print("Full/Part time   :",self.type_job)

class full_Time(employee):
    def calculate_pay(self,working_hrs=0):
        self.working_hrs = working_hrs
        self.epf = (self.pay * 12 / 100)
        self.allowance = 0
        if self.shift.lower() == "night" and working_hrs > 9:
                    self.allowance = (self.pay * 12 / 100)
        elif self.shift.lower() == "day" and working_hrs > 9:
             self.allowance = (self.pay * 6 / 100)
        else:
            self.pay = self.pay
        self.salary = ((self.pay - self.epf) + self.allowance)

        print("           Salary Sheet       ")
        print("--------------------------------")
        print("Name of Employee   : ",self.name)
        print("Employee ID        : ",self._id)
        print("--------------------------------")
        print("Basic Pay-Monthly  : ₹ ",self.pay)
        print("Allowance          : ₹ ",self.allowance)
        print("EPF                : ₹ ",self.epf)
        print("--------------------------------")
        print("Salary in Hand     : ₹ ",self.salary)
        print("--------------------------------")


        
class part_Time(employee):
    def calculate_pay(self,working_hrs=0):
        self.working_hrs = working_hrs
        

        if self.shift.lower() == "night" and working_hrs > 5:
                    self.allowance = (self.pay * 6 / 100)
        elif self.shift.lower() == "day" and working_hrs > 5:
             self.allowance = (self.pay * 3 / 100)
        else:
            self.pay = self.pay
        self.salary = (self.pay  + self.allowance)

        print("           Salary Sheet       ")
        print("--------------------------------")
        print("Employee ID       : ",self._id)
        print("Name of Employee  : ",self.name)
        print("--------------------------------")
        print("Basic Pay- Hour   : ₹ ",self.pay)
        print("Allowance         : ₹ ",self.allowance)
        print("--------------------------------")
        print("Salary in Hand    : ₹ ",self.salary)
        print("--------------------------------")
        
        
Vijay = full_Time(201,"Vijay","2023-05-15","Day","1992-03-10",32,70000,"FullTime")

Karthi = full_Time(202,"Karthi","2022-08-20","Night","1988-06-25",36,80000,"FullTime")



Jack = part_Time(301,"Jack","2024-02-10","Day","1995-12-05",28,400,"PartTime")

Gukesh = part_Time(302,"Gukesh","2023-11-01","Night","1990-07-18",34,1000,"PartTime")


print("Full Time")

Vijay.display_full_report()

print("")

Vijay.calculate_pay()

print("")
print("")

print("Part Time")

Gukesh.display_full_report()

print("")
print("")

Gukesh.calculate_pay(10)
