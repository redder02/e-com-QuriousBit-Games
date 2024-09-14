
# this class would be having all the product details
class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category


# this class will be responsible for individual items of the class
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    #calculating total price based on quantity and price
    def total_price(self):
        return self.product.price * self.quantity


# current situation of the cart
class Cart:
    def __init__(self):
        self.items = []

    # adding item into the cart
    def add_item(self, product, quantity):

        # checking if item is already present in the cart
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        # if item is not present in cart then add to the list
        self.items.append(CartItem(product, quantity))

    # removing items from the cart
    def remove_item(self, product_id, quantity=None):

        
        for item in self.items:

            # if product quantity not given by customer then remove all the products 
            if item.product.product_id == product_id:
                if quantity is None or quantity >= item.quantity:
                    self.items.remove(item)
                else:
                    item.quantity -= quantity # if quantity specified then reduce that much quantity only
                return

    # current cart snapshot
    def view_cart(self):
        total_cost = 0
        print("Your Cart:")
        for item in self.items:
            total = item.total_price()
            total_cost += total
            print(f"{item.product.name} - Quantity: {item.quantity}, Price: {item.product.price:.2f} USD, Total: {total:.2f} USD")
        print(f"Total (before discounts): {total_cost:.2f} USD")
        return total_cost
