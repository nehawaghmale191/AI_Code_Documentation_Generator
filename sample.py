# Standalone helper function
def format_currency(amount: float) -> str:
    """Formats a float value into a currency string standard."""
    return f"${amount:.2f}"


class Product:
    """Represents an item available for purchase."""
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_details(self) -> str:
        """Returns a string description of the product."""
        return f"{self.name} - {format_currency(self.price)}"


class ShoppingCart:
    """Manages a collection of products and handles calculation tasks."""
    
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.items = []  # Stores Product objects

    def add_item(self, product: Product):
        """Adds a product to the shopping cart."""
        self.items.append(product)
        print(f"Added {product.name} to {self.customer_name}'s cart.")

    def calculate_total(self, tax_rate: float = 0.05) -> float:
        """Calculates total price including a default tax rate of 5%."""
        subtotal = sum(item.price for item in self.items)
        tax = subtotal * tax_rate
        return subtotal + tax

    def display_receipt(self):
        """Prints an organized summary of items and final costs."""
        print(f"\n--- Receipt for {self.customer_name} ---")
        for item in self.items:
            # Calling a method on a product object inside the class
            print(item.get_details())
        
        final_total = self.calculate_total()
        # Using the standalone function inside the class method
        print(f"Total Bill (inc. tax): {format_currency(final_total)}")
        print("-" * 30)


# Execution block to see the code in action
if __name__ == "__main__":
    # 1. Instantiate Product objects
    laptop = Product("Laptop", 999.99)
    mouse = Product("Wireless Mouse", 25.50)

    # 2. Instantiate a ShoppingCart object
    my_cart = ShoppingCart("Alice")

    # 3. Use class methods to add items and print receipts
    my_cart.add_item(laptop)
    my_cart.add_item(mouse)
    my_cart.display_receipt()