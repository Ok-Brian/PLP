# Base Class
class Smartphones:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def browse(self):
        return f"{self.brand} {self.model} is browsing the internet."

    def battery_status(self):
        return f"Battery life: {self.battery_life} hours left."


# Inherited Class (Polymorphism Example)
class SmartphonePro(Smartphones):
    def __init__(self, brand, model, battery_life, camera_quality):
        super().__init__(brand, model, battery_life)
        self.camera_quality = camera_quality  # in megapixels

    # Override (Polymorphism) → extend behavior
    def browse(self):
        return f"{self.brand} {self.model} is browsing at 5G speed!"

    def take_photo(self):
        return f"Taking a {self.camera_quality}MP photo with {self.brand} {self.model}."


# --- Main Program ---
# Create base class object
phone1 = Smartphones("Nokia", "3310", 48)
print(phone1.call("123456789"))
print(phone1.browse())
print(phone1.battery_status())

print("------")

# Create inherited class object
phone2 = SmartphonePro("Apple", "iPhone 11 Pro", 20, 48)
print(phone2.call("987654321"))
print(phone2.browse())   # Polymorphic behavior
print(phone2.take_photo())
print(phone2.battery_status())

# Creating another inherited class object
phone3 = SmartphonePro("Samsung", "Galaxy S20", 24, 64)
print(phone3.call("555555555"))
print(phone3.browse())   # Polymorphic behavior 