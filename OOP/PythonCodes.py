class FoodOrder:  # creating a class named FoodOrder
    def __init__(self, customer_name, item, price): # defining the constructor method to initialize the attributes of the class
        self.customer_name = customer_name # assigning the value of customer_name to the instance variable
        self.item = item
        self.price = price

    def show_order(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Item: {self.item}")
        print(f"Price: {self.price}")

order1 = FoodOrder("Bijena", "Pizza", 15.99) # passing the values to the constructor
order2 = FoodOrder("John", "Burger", 9.99)
print(order1.customer_name, order1.item, order1.price) # accessing the customer_name attribute of order1
print(order2.customer_name, order2.item, order2.price) # accessing the item attribute of order2
order1.show_order() # calling the show_order method of order1
'''
inside class: only defining the class and its attributes and methods
outside class: creating objects and accessing the attributes and methods of the class'''

# suppose you are working for daraz application and u have to work for new brand of laptop
# create a class Laptop with brand, price and method show_details() ,
print("--------------------------------------------------------------")
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")

laptop1 = Laptop("Dell", 80000)
laptop2 = Laptop("HP", 75000)
laptop1.show_details()
laptop2.show_details()