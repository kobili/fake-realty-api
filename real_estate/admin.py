from django.contrib import admin

from .models import Address, Property
from .fake_factories import Property as FakeProperty


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "address_line_1",
        "address_line_2",
        "unit_number",
        "city",
        "province",
        "post_code",
        "country",
    ]

class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        "mls",
        "monthly_rent",
        "purchase_price",
        "square_footage",
        "bedrooms",
        "bathrooms",
        "title",
    ]

    fields = [
        "mls",
        ("monthly_rent", "purchase_price"),
        ("square_footage", "bedrooms", "bathrooms"),
        "title",
        "amenities",
        "address",
    ]

    actions = ["generate_new_property"]

    @admin.action(description="Generate a new property listing")
    def generate_new_property(self, request, queryset):
        new_property = FakeProperty().to_dict()
        new_address = new_property.pop("address")

        addr = Address.objects.create(**new_address)
        Property.objects.create(address=addr, **new_property)


# Register your models here.
admin.site.register(Address, AddressAdmin)
admin.site.register(Property, PropertyAdmin)
