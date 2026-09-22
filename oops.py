# class Student:
#     def __init__(self, name, age, course):
#          self.name = name
#          self.age = age
#          self.course = course


# s1 = Student("Riya", 20, "B.Tech")
# s2 = Student("Roshan", 23, "BCA")

# print(s1.age)
# print(s2.name)

# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price


# my_car = Car("Audi", "A6", 600000)

# print(my_car.brand)



class Account:
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

U1 = Account("Riya", 500)

U1.withdraw(50)

print(U1.balance)



