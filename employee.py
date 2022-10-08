"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, isHourly, salary, commisionPay = 0, commisionContracts = 0, hours = 0):
        self.name = name
        self.isHourlyContract = isHourly
        if self.isHourlyContract:
            self.hours = hours

        self.salary = salary
        self.commisionPay = commisionPay
        self.commisionContracts = commisionContracts



    def get_pay(self):
        pay = 0
        if self.isHourlyContract:
            pay = self.salary * self.hours
        else:
            pay = self.salary

        if self.commisionPay != 0:
            if self.commisionContracts != 0:
                pay += self.commisionPay * self.commisionContracts
            else:
                pay += self.commisionPay

        return pay


    def __str__(self):
        
  
        # return f"{self.name} works on a monthly of {self.salary}.  Their total pay is {self.get_pay()}."

        if self.isHourlyContract:
            if self.commisionContracts == 0 and self.commisionPay == 0:
                return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour.  Their total pay is {self.get_pay()}."
            if self.commisionContracts == 0 and self.commisionPay != 0:
                return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a bonus commission of {self.commisionPay}.  Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a commission for {self.commisionContracts} contract(s) at {self.commisionPay}/contract.  Their total pay is {self.get_pay()}."
        else:
            if self.commisionContracts == 0 and self.commisionPay == 0:
                return f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.get_pay()}."
            if self.commisionContracts == 0 and self.commisionPay != 0:
                return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commisionPay}.  Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.commisionContracts} contract(s) at {self.commisionPay}/contract.  Their total pay is {self.get_pay()}."



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', False, 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', True, 25, 0, 0, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', False, 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', True, 25, 220, 3, 150)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', False, 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', True, 30, 600, 0, 120)
