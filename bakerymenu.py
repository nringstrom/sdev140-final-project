# Import necessary dependencies
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialize the application in tkinter, deploy each window and define values.
class BakeryApp:
    def __init__(self, master):
        # Initialize master window
        self.master = master
        self.master.title("Bakery Ordering System")  # Set window title
        self.master.configure(bg="aquamarine")  # Set background color
        
        # Define bakery items and their details
        self.items = {
            "Croissant": {"price": 2.00, "image": "croissant.png"},
            "Muffin": {"price": 1.50, "image": "muffin.png"},
            "Baguette": {"price": 3.00, "image": "baguette.png"},
            "Cupcake": {"price": 2.50, "image": "cupcake.png"}
        }
        self.cart = {}  # Initialize empty cart
        
        # Create order and checkout windows
        self.create_order_window()
        self.create_checkout_window()
        
    # Create order window to display bakery items
    def create_order_window(self):
        self.order_window = tk.Toplevel(self.master)
        self.order_window.title("Order Items")  # Set window title
        self.order_window.configure(bg="aquamarine")  # Set background color
        
        self.quantity_entries = {}  # Initialize dictionary to store quantity entries
        
        # Loop through each bakery item and create corresponding UI elements
        for i, (item, details) in enumerate(self.items.items()):
            # Load item image
            image = Image.open(details["image"])
            photo = ImageTk.PhotoImage(image)
            
            # Create label to display item name, price, and image
            label = tk.Label(self.order_window, text=f"{item} - ${details['price']:.2f}", image=photo, compound=tk.LEFT, bg="aquamarine", fg="black")
            label.image = photo  # Keep reference to the image to avoid garbage collection
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            
            # Create entry for quantity input
            quantity_entry = tk.Entry(self.order_window, width=5, bg="white", fg="black")
            quantity_entry.grid(row=i, column=1, padx=5, pady=5)
            self.quantity_entries[item] = quantity_entry
            
            # Create buttons for adjusting quantity and adding to cart
            add_button = tk.Button(self.order_window, text="+", command=lambda q=quantity_entry: self.increment_quantity(q), bg="white", fg="black")
            add_button.grid(row=i, column=2, padx=5, pady=5, sticky="w")
            
            minus_button = tk.Button(self.order_window, text="-", command=lambda q=quantity_entry: self.decrement_quantity(q), bg="white", fg="black")
            minus_button.grid(row=i, column=3, padx=5, pady=5, sticky="w")
            
            add_to_cart_button = tk.Button(self.order_window, text="Add to Cart", command=lambda i=item, q=quantity_entry: self.add_to_cart(i, q), bg="white", fg="black")
            add_to_cart_button.grid(row=i, column=4, padx=5, pady=5, sticky="w")
        
        # Create button to show cart
        cart_button = tk.Button(self.order_window, text="Cart", command=self.show_checkout_window, bg="white", fg="black")
        cart_button.grid(row=len(self.items), column=0, columnspan=5, padx=10, pady=10, sticky="ew")
            
    # Create checkout window to display cart items
    def create_checkout_window(self):
        self.checkout_window = tk.Toplevel(self.master)
        self.checkout_window.title("Checkout")  # Set window title
        self.checkout_window.withdraw()  # Hide the checkout window
        self.checkout_window.configure(bg="aquamarine")  # Set background color
        
        # Create label for cart items
        self.checkout_label = tk.Label(self.checkout_window, text="Items in Cart:", bg="aquamarine", fg="black")
        self.checkout_label.pack(pady=10)
        
        # Create listbox to display cart items
        self.checkout_listbox = tk.Listbox(self.checkout_window, width=50, bg="white", fg="black")
        self.checkout_listbox.pack()
        
        # Create button to complete checkout
        checkout_button = tk.Button(self.checkout_window, text="Complete Checkout", command=self.complete_checkout, bg="white", fg="black")
        checkout_button.pack(pady=10)
        
    # Add item to cart
    def add_to_cart(self, item, quantity_entry):
        quantity_str = quantity_entry.get()
        if quantity_str.isdigit() and int(quantity_str) > 0:
            quantity = int(quantity_str)
            if item in self.cart:
                self.cart[item] += quantity
            else:
                self.cart[item] = quantity
            self.update_checkout_listbox()  # Update cart display
        else:
            messagebox.showerror("Error", "Please enter a valid quantity.")
    
    # Update cart listbox with current items
    def update_checkout_listbox(self):
        self.checkout_listbox.delete(0, tk.END)
        for item, quantity in self.cart.items():
            self.checkout_listbox.insert(tk.END, f"{item} - Quantity: {quantity}")
            
    # Finalize checkout
    def complete_checkout(self):
        total_price = sum(self.items[item]["price"] * quantity for item, quantity in self.cart.items())
        messagebox.showinfo("Checkout Complete", f"Total Price: ${total_price:.2f}")
        self.cart.clear()  # Clear cart
        self.update_checkout_listbox()  # Update cart display
        
    # Show checkout window
    def show_checkout_window(self):
        self.checkout_window.deiconify()  
        
    # Increment quantity
    def increment_quantity(self, quantity_entry):
        current_quantity_str = quantity_entry.get()
        current_quantity = int(current_quantity_str) if current_quantity_str else 0
        new_quantity = current_quantity + 1
        quantity_entry.delete(0, tk.END)
        quantity_entry.insert(0, str(new_quantity))

    # Decrement quantity
    def decrement_quantity(self, quantity_entry):
        current_quantity_str = quantity_entry.get()
        current_quantity = int(current_quantity_str) if current_quantity_str else 0
        if current_quantity > 0:
            new_quantity = current_quantity - 1
            quantity_entry.delete(0, tk.END)
            quantity_entry.insert(0, str(new_quantity))

# Main function to run the application
def main():
    root = tk.Tk()  # Create tkinter root window
    app = BakeryApp(root)  # Initialize BakeryApp instance
    root.mainloop()  # Start tkinter event loop

# Execute main function if script is run directly
if __name__ == "__main__":
    main()
