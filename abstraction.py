from abc import ABC, abstractmethod # importing ABC module
class Groceries(ABC): # parent class
    def milk(self, amount):
        print("The price of milk is: ", amount)

    def bread(self, amount):
        print("The price of bread is: ", amount)

    @abstractmethod
    def total(self, amount): # abstract method
        pass

class totalCost(Groceries): # child class inherits "total" from parent class
    def total(self, amount):
        print("Your total cost for groceries today is {}.".format(amount))


cost = totalCost()
cost.milk("$4")
cost.bread("$3") # here we define the amounts for milk, bread, and total 
cost.total("$7")
