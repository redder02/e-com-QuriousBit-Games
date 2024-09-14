class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_id, quantity=None):
        for item in self.items:
            if item.product.product_id == product_id:
                if quantity is None or quantity >= item.quantity:
                    self.items.remove(item)
                else:
                    item.quantity -= quantity
                return


    def view_cart(self):
        total_cost = 0
        print("Your Cart:")
        for item in self.items:
            total = item.total_price()
            total_cost += total
            print(f"{item.product.name} - Quantity: {item.quantity}, Price: {item.product.price:.2f} USD, Total: {total:.2f} USD")
        print(f"Total (before discounts): {total_cost:.2f} USD")
        return total_cost
