from django.contrib import admin

from .models import Address, Property


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


# Register your models here.
admin.site.register(Address, AddressAdmin)
admin.site.register(Property, PropertyAdmin)
