import unittest
from device_manager import Device, MobilePhone, Laptop, Television, Inventory, Customer, Order

class TestDeviceManager(unittest.TestCase):

    # Test za klasu MobilePhone
    def test_mobile_phone_initialization(self):
        phone = MobilePhone("Samsung", 999.99, 10, "Android", 128)
        self.assertEqual(phone.brand, "Samsung")
        self.assertEqual(phone.price, 999.99)
        self.assertEqual(phone.quantity, 10)
        self.assertEqual(phone.operating_system, "Android")
        self.assertEqual(phone.storage_capacity, 128)

    def test_mobile_phone_get_details(self):
        phone = MobilePhone("iPhone", 1299.99, 5, "iOS", 256)
        expected_details = "MobilePhone: iPhone, OS: iOS, Storage: 256GB, Price: $1299.99, Stock: 5"
        self.assertEqual(phone.get_details(), expected_details)

    # Test za klasu Laptop
    def test_laptop_get_details(self):
        laptop = Laptop("Dell", 899.99, 8, "Intel i5", 16)
        expected_details = "Laptop: Dell, Processor: Intel i5, RAM: 16GB, Price: $899.99, Stock: 8"
        self.assertEqual(laptop.get_details(), expected_details)

    # Test za klasu Television
    def test_television_get_details(self):
        tv = Television("LG", 499.99, 15, 55, True)
        expected_details = "Television: LG, Screen: 55\" Smart TV, Price: $499.99, Stock: 15"
        self.assertEqual(tv.get_details(), expected_details)

    # Test za klasu Inventory
    def test_inventory_add_and_remove_device(self):
        inventory = Inventory()
        phone = MobilePhone("OnePlus", 699.99, 20, "Android", 256)
        inventory.add_device(phone)
        self.assertIn(phone, inventory.devices)
        
        inventory.remove_device("OnePlus")
        self.assertNotIn(phone, inventory.devices)

    def test_inventory_update_device_quantity(self):
        inventory = Inventory()
        phone = MobilePhone("OnePlus", 699.99, 20, "Android", 256)
        inventory.add_device(phone)
        
        result = inventory.update_device_quantity("OnePlus", 10)
        self.assertEqual(result, "Updated OnePlus quantity to 10")
        self.assertEqual(phone.quantity, 10)

    # Test za klasu Customer
    def test_customer_add_order(self):
        customer = Customer("John Doe", "123456789", "123 Elm Street", "john@example.com")
        order = Order(customer)
        customer.add_order(order)
        self.assertIn(order, customer.orders)

    def test_customer_calculate_total_spent(self):
        customer = Customer("Jane Doe", "987654321", "456 Oak Avenue", "jane@example.com")
        phone = MobilePhone("iPhone", 1299.99, 5, "iOS", 256)
        order = Order(customer)
        order.add_product(phone, 2)
        customer.add_order(order)
        
        total_spent = customer.calculate_total_spent()
        self.assertEqual(total_spent, 2599.98)

    # Test za klasu Order
    def test_order_add_product(self):
        customer = Customer("John Doe", "123456789", "123 Elm Street", "john@example.com")
        phone = MobilePhone("Samsung", 999.99, 10, "Android", 128)
        order = Order(customer)
        
        order.add_product(phone, 2)
        self.assertEqual(len(order.products), 1)
        self.assertEqual(phone.quantity, 8)

    def test_order_calculate_total(self):
        customer = Customer("Jane Doe", "987654321", "456 Oak Avenue", "jane@example.com")
        phone = MobilePhone("iPhone", 1299.99, 5, "iOS", 256)
        laptop = Laptop("Dell", 899.99, 8, "Intel i5", 16)
        order = Order(customer)
        
        order.add_product(phone, 1)
        order.add_product(laptop, 1)
        total = order.calculate_total()
        self.assertEqual(total, 2199.98)

    def test_order_apply_discount(self):
        customer = Customer("John Doe", "123456789", "123 Elm Street", "john@example.com")
        phone = MobilePhone("Samsung", 999.99, 10, "Android", 128)
        order = Order(customer)
        
        order.add_product(phone, 2)
        discounted_total = order.apply_discount(10)  # 10% popusta
        self.assertAlmostEqual(discounted_total, 1799.98, places=2)


if __name__ == "__main__":
    unittest.main()
