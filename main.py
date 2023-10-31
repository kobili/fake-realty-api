from random import randint
from string import ascii_uppercase, digits

from faker import Faker
from faker.providers import BaseProvider

faker = Faker()

class PropertyFakerProvider(BaseProvider):
    def street_number(self):
        return randint(100, 999)
    
    def street_type(self):
        types = ["St", "Dr", "Ave", "Blvd"]
        idx = randint(0, len(types)-1)
        return types[idx]
    
    def unit_number(self):
        apartment = randint(1, 100) < 50
        
        return "" if not apartment else str(randint(1, 5000))
    
    def province(self):
        provinces = [
            "British Columbia",
            "Alberta",
            "Ontario",
            "Quebec",
            "Nova Scotia",
            "New Brunswick",
            "Manitoba",
            "Prince Edward Island",
            "Saskatchewan",
            "Newfoundland and Laborador",
        ]

        return provinces[randint(0, len(provinces)-1)]
    
    def post_code(self):
        return f"{self._random_upper()}{self._random_digit()}{self._random_upper()} {self._random_digit()}{self._random_upper()}{self._random_digit()}"
    
    def _random_upper(self):
        return ascii_uppercase[randint(0, len(ascii_uppercase)-1)]
    def _random_digit(self):
        return digits[randint(0, len(digits)-1)]
    
faker.add_provider(PropertyFakerProvider)

class Address:
    def __init__(self):
        self.address_line_1 = f"{faker.street_number()} {faker.name()} {faker.street_type()}"
        self.address_line_2 = ""
        self.unit_number = faker.unit_number()
        self.city = faker.city()
        self.province = faker.province()
        self.post_code = faker.post_code()
        self.country = "Canada"


    def to_dict(self):
        return {
            "address_line_1": self.address_line_1,
            "address_line_2": self.address_line_2,
            "unit_number": self.unit_number,
            "city": self.city,
            "province": self.province,
            "post_code": self.post_code,
            "country": self.country,
        }

class Property:
    def __init__(self):
        self.address = Address()
    
    def to_dict(self):
        return {
            "address": self.address.to_dict(),
        }

for i in range(0, 5):
    prop = Property()
    print(prop.to_dict())
