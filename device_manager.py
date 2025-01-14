from abc import ABC, abstractmethod
from datetime import datetime

# Apstraktna klasa Device
class Device(ABC):
    def __init__(self, brand, price, quantity):
        self.brand = brand
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_details(self):
        pass

# Klasa MobilePhone
class MobilePhone(Device):
    def __init__(self, brand, price, quantity, operating_system, storage_capacity):
        super().__init__(brand, price, quantity)
        self.operating_system = operating_system
        self.storage_capacity = storage_capacity

    def get_details(self):
        return f"MobilePhone: {self.brand}, OS: {self.operating_system}, Storage: {self.storage_capacity}GB, Price: ${self.price}, Stock: {self.quantity}"

# Klasa Laptop
class Laptop(Device):
    def __init__(self, brand, price, quantity, processor, ram):
        super().__init__(brand, price, quantity)
        self.processor = processor
        self.ram = ram

    def get_details(self):
        return f"Laptop: {self.brand}, Processor: {self.processor}, RAM: {self.ram}GB, Price: ${self.price}, Stock: {self.quantity}"

# Klasa Television
class Television(Device):
    def __init__(self, brand, price, quantity, screen_size, is_smart):
        super().__init__(brand, price, quantity)
        self.screen_size = screen_size
        self.is_smart = is_smart

    def get_details(self):
        smart_status = "Smart TV" if self.is_smart else "Non-Smart TV"
        return f"Television: {self.brand}, Screen: {self.screen_size}\" {smart_status}, Price: ${self.price}, Stock: {self.quantity}"

# Klasa Inventory
class Inventory:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, brand):
        self.devices = [device for device in self.devices if device.brand != brand]

    def update_device_quantity(self, brand, quantity):
        for device in self.devices:
            if device.brand == brand:
                device.quantity = quantity
                return f"Updated {brand} quantity to {quantity}"
        return f"Device {brand} not found."

    def display_inventory(self):
        for device in self.devices:
            print(device.get_details())

# Klasa Customer
class Customer:
    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_spent(self):
        return sum(order.calculate_total() for order in self.orders)

# Klasa Order
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = []
        self.date = datetime.now()
        self.status = "Pending"

    def add_product(self, device, quantity):
        if device.quantity >= quantity:
            device.quantity -= quantity
            self.products.append((device, quantity))
        else:
            print(f"Not enough stock for {device.brand}.")

    def calculate_total(self):
        return sum(device.price * quantity for device, quantity in self.products)

    def apply_discount(self, discount_percent):
        total = self.calculate_total()
        return total - (total * discount_percent / 100)

    def print_order_summary(self):
        print(f"Order for {self.customer.name} on {self.date}")
        for device, quantity in self.products:
            print(f"{device.brand} x{quantity} - ${device.price * quantity}")
        print(f"Total: ${self.calculate_total()}")
        print(f"Status: {self.status}")
