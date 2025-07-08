# inventory_utils.py
import random

def restock(products_dict):
    for p in products_dict.values():
        restock_amount = random.randint(1, 10)
        p['quantity'] += restock_amount
