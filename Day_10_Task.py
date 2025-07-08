# Inventory Manager Using OOP, Lambda, and Comprehensions

import random
from inventory_utils import restock

# Base class Product
class Product:
    def __init__ (self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity =quantity
    
    def total_value(self):
        return self.price * self.quantity
        
# Sub class PerishableProduct
class PerishableProduct(Product):
    def __init__(self,name, price, quantity, expiry_days):
        super().__init__(name, price, quantity)
        self.expiry_days = int(expiry_days)
        
    def total_value(self):
        base_value = super().total_value()

        if self.expiry_days < 5:
            total_value = base_value * 0.8
            return total_value
        else:
            return base_value

class InventoryManager:
    def __init__(self):
        self.products = {}
        
    def add_product(self, name, price, quantity, expiry_days = None):
        self.products[name] = {'price' : price, "quantity" : quantity }
           
    def list_inventory(self):
        if not self.products:
            print("Empty inventory list.")
        else:
            for index, (key , value) in enumerate(self.products.items()):
             print(f" {index+1}. {key} : {value}")
            
    def search_product(self, product_name):
        if product_name not in self.products:
            print(f"{product_name} is not present in inventory.")
        else:
            get_product = lambda p : self.products[p]
            product = get_product(product_name)
            print(f"Product : {product} \n 'price' : {product['price']}, 'quantity' : {product['quantity']}")
      
    def restock_all(self):
        restock(self.products)
        print("All products are restocked.")       
        
    def export_report(self, filename="inventory_report.txt"):
        with open(filename, "w") as f:
            [f.write(f"{name}: {info}\n") for name, info in self.products.items()]
        print(f"📄 Report exported to {filename}")
    
def main():
    manager = InventoryManager()
    while True:
        print("\nWelcome to InventoryManager")
        print("1. Add Product ")
        print("2. List_inventory ")
        print("3. Search_by_name ")
        print("4. Restock_all ") 
        print("5. Export Inventory Report")
        print("6. Exit ") 

        user_choice = int(input("Enter your choice : "))  

        if user_choice == 1 :
            name = input("Enter the name of product : ")
            price = float(input("Enter the price of product : "))
            quantity = int(input("Enter the quantity of product : "))
            expiry = (input("Is it perishabel product : (yes/no)")).lower()

            if expiry == 'yes':
                expiry_days = int(input("Enter the expiry days : "))
                product = PerishableProduct(name, price, quantity, expiry_days)
                manager.products[name] = {
                    'price' : price,
                    'quantity' : quantity,
                    'expiry_days' : expiry_days,
                    'discounted_value' : product.total_value()
                }
            else:
                manager.add_product(name, price, quantity)

        elif user_choice == 2:
            manager.list_inventory()
        
        elif user_choice == 3:
            user_search_product = input("Enter the product that you want to search : ")
            manager.search_product(user_search_product)
    
        elif user_choice == 4:
           manager.restock_all()
    
        elif user_choice == 5:
            manager.export_report()
            
        elif user_choice == 6:
            print("Exiting InventoryManager. Bye!")
            break
        
        else:
            print(f'Invalid choice. Try again.')

main()