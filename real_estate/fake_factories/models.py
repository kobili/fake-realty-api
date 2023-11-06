from fake_factories import Faker

from fake_factories.providers import AddressFakerProvider, PropertyFakerProvider

class Address:
    def __init__(self):
        faker = Faker()
        faker.add_provider(AddressFakerProvider)

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
        faker = Faker()
        faker.add_provider(PropertyFakerProvider)

        self.mls = faker.mls()

        monthly_rent, purchase_price = faker.prices()
        self.monthly_rent = monthly_rent
        self.purchase_price = purchase_price
        # ^ one of these will be None

        self.square_footage = faker.square_footage()
        self.bedrooms = faker.bedroom_count()
        self.bathrooms = faker.bathroom_count()

        self.title = faker.title()
        self.amenities = faker.amenities()

        self.address = Address()
    
    def to_dict(self):
        return {
            "mls": self.mls,
            "monthly_rent": self.monthly_rent,
            "purchase_price": self.purchase_price,
            "address": self.address.to_dict(),
            "square_footage": self.square_footage,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "title": self.title,
            "amenities": self.amenities,
        }
