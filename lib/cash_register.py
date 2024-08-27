#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction_amount = 0
  def add_item(self, title, price, quantity=1):
    self.title = title
    self.last_transaction_amount = price * quantity
    self.total += self.last_transaction_amount
    self.quantity = quantity
    self.items.extend([title] * quantity)
  def apply_discount(self):
    if self.discount > 0:
        discount = self.total * (self.discount / 100)
        self.total = self.total - discount
        print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
  def void_last_transaction(self):
    self.total -= self.last_transaction_amount
    self.last_transaction_amount = 0