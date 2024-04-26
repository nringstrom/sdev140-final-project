import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class BakeryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bakery Ordering System")
        
        self.items = {
            "Croissant": {"price": 2.00, "image": "croissant.png"},
            "Muffin": {"price": 1.50, "image": "muffin.png"},
            "Baguette": {"price": 3.00, "image": "baguette.png"},
            "Cupcake": {"price": 2.50, "image": "cupcake.png"}
        }
        self.cart = {}
        
        self.create_order_window()
        self.create_checkout_window()
        
    def create_order_window(self):
        self.order_window = tk.Toplevel(self.master)
        self.order_window.title("Order Items")
        
        for i, (item, details) in enumerate(self.items.items()):
            image = Image.open(details["image"])
            image = image.resize((50, 50), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            
            label = tk.Label(self.order_window, text=f"{item} - ${details['price']:.2f}", image=photo, compound=tk.LEFT)
            label.image = photo  # keep a reference to the image to avoid garbage collection
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            
            quantity_entry = tk.Entry(self.order_window, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            
            add_button = tk.Button(self.order_window, text="Add", command=lambda i=item: self.add_to_cart(i, quantity_entry))
            add_button.grid(row=i, column=2, padx=10, pady=5)
            
    def create_checkout_window(self):
        self.checkout_window = tk.Toplevel(self.master)
        self.checkout_window.title("Checkout")
        
        self.checkout_label = tk.Label(self.checkout_window, text="Items in Cart:")
        self.checkout_label.pack(pady=10)
        
        self.checkout_listbox = tk.Listbox(self.checkout_window, width=50)
        self.checkout_listbox.pack()
        
        checkout_button = tk.Button(self.checkout_window, text="Complete Checkout", command=self.complete_checkout)
        checkout_button.pack(pady=10)
        
        
def main():
    root = tk.Tk()
    app = BakeryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
