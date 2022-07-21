class CashRegister:

    def __init__(self):
        self.total_items = {}  # {'item': 'price'}
        self.discount = 0

    def add_item(self, item_and_price):
        """This function updates the dict to add new items and the price"""
        self.total_items.update(item_and_price)

    def remove_item(self, item):
        """This function removes the item from the Cash Register"""
        self.total_items.pop(item)

    def apply_discount(self, percentage):
        """This function applies a percentage discount. The percentage is taken from the total price.
        For example, you would be able to specify a 50% discount, and this will apply this to
        the total price of the cash register, rather than the individual items. I chose to choose
        this way of applying discount, as this is more common within stores during sales"""
        total_price = sum(self.total_items.values())
        self.discount = total_price * percentage / 100

    def get_total(self):
        """This function gets a total of the Cash Register before any discount is applied,
        and then subtracts the discount for the actual total amount. This function also
        shows the total amount saved from any discounts applied."""
        total_before_discount = sum(self.total_items.values())
        total = total_before_discount - self.discount
        return f"Total: {total_before_discount:.2f} \nYou saved {self.discount:.2f}! \nAmount Left to Pay: {total:.2f} "

    def show_items(self):
        """This function prints the items in the Cash Register"""
        for item, price in self.total_items.items():
            print(f" Item: {item} \n Price: £{price:.2f}")

    def reset_register(self):
        """This function resets the register (clears it for a new user)"""
        self.total_items = {}
        self.discount = 0

# Example of how my code works:
# The first customer is using the Cash Register:
customer_1 = CashRegister()

# Suppose Customer 1 is shopping at Asos for their holiday, and scans their items:

customer_1.add_item({'ASOS Design Pink Dress': 35.00})
customer_1.add_item({'New Look Brown Sandals': 15.00})
customer_1.add_item({'ASOS Design Denim Shorts': 25.00})
customer_1.add_item({'Pull&Bear Round Sunglasses': 13.00})
customer_1.add_item({'Garnier Gradual Tan': 10.00})
customer_1.add_item({'New Look Black Sandals': 15.00})

# Customer 1 has noticed that they added Sandals to their register twice
# They need to remove this item:

customer_1.remove_item('New Look Black Sandals')

# Customer 1 has just found out that Asos are having a holiday sale
# They are offering customers 40% off their basket
# Customer 1 applies the discount:

customer_1.apply_discount(40)

# Customer 1 would like to see their items, their total basket price, and how much they saved:

customer_1.show_items()
print(customer_1.get_total())

# Customer 1 has now finished at the Cash Register and the Cash Register is cleared:

customer_1.reset_register()

# Customer 2 would now like to buy some items for their holiday:

customer_2 = CashRegister()

# Customer 2 adds their items to the Cash Register:

customer_2.add_item({'QUAY Sunglasses': 49.00})
customer_2.add_item({'ASOS Design Swim Shorts': 16.00})
customer_2.add_item({'Topman Black Shorts': 20.00})
customer_2.add_item({'Ralph Lauren Polo': 95.00})

# Customer 2 also takes advantage of the 40% discount:

customer_2.apply_discount(40)

# Customer 2 would like to see their items, their total basket price, and how much they saved:

customer_2.show_items()
print(customer_2.get_total())

# The Cash Register is cleared ready for the next customer

customer_2.reset_register()