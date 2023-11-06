from random import randint, uniform as rand_uniform, choice
from string import ascii_uppercase, digits

from faker.providers import BaseProvider


def random_upper():
    return choice(ascii_uppercase)
def random_digit():
    return choice(digits)

class AddressFakerProvider(BaseProvider):
    def street_number(self):
        return randint(100, 999)

    def street_type(self):
        return choice(["St", "Dr", "Ave", "Blvd"])

    def unit_number(self):
        apartment = randint(1, 100) < 50

        return "" if not apartment else str(randint(1, 5000))

    def province(self):
        return choice([
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
        ])

    def post_code(self):
        return f"{random_upper()}{random_digit()}{random_upper()} {random_digit()}{random_upper()}{random_digit()}"


class PropertyFakerProvider(BaseProvider):
    def mls(self):
        mls = "R"
        for _ in range(0, 7):
            mls += random_digit()

        return mls

    def prices(self) -> tuple:
        """
        Returns a tuple of (monthly_rent, purchase_price), one of which will be None
        """
        is_rent_price = randint(0, 1) == 0

        if is_rent_price:
            return (round(rand_uniform(2.0, 3.0), 2) * 1000, None)
        
        return (None, round(rand_uniform(0.5, 2.5), 2) * 1_000_000)

    def square_footage(self):
        return randint(4, 20) * 100
    
    def bathroom_count(self):
        return randint(1, 3)
    
    def bedroom_count(self):
        return randint(1, 4)

    def title(self):
        return choice(["strata", "leasehold"])

    def amenities(self):
        types = ["gym", "pool", "rec_room", "meeting_room", "common_area"]
        selections = [0] * len(types)
        for i in range(0, len(types)):
            selections[i] = randint(1, 100) < 50

        result = []
        for i in range(0, len(types)):
            if selections[i]:
                result.append(types[i])

        return result