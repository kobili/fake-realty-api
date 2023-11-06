from django.db.models import TextChoices

class CanadianProvinces(TextChoices):
    BRITISH_COLUMBIA = "BC", "British Columbia"
    ALBERTA = "AB", "Alberta"
    ONTARIO = "ON", "Ontario"
    QUEBEC = "QC", "Quebec"
    NOVA_SCOTIA = "NS", "Nova Scotia"
    NEW_BRUNSWICK = "NB", "New Brunswick"
    MANITOBA = "MB", "Manitoba"
    PEI = "PE", "Prince Edward Island"
    SASKATCHEWAN = "SK", "Saskatchewan"
    NEWFOUNDLAND = "NL", "Newfoundland and Laborador"
    YUKON = "YT", "Yukon"
    NORTHWEST_TERRITORIES = "NT", "Northwest Territories"
    NUNAVUT = "NU", "Nunavut"

class PropertyTitleTypes(TextChoices):
    STRATA = "strata", "Strata"
    LEASEHOLD = "leasehold", "Leasehold"
