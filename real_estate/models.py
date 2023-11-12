from django.db import models
from .constants import CanadianProvinces, PropertyTitleTypes


# Create your models here.
class Address(models.Model):
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, default="")
    unit_number = models.CharField(max_length=4, blank=True, null=True)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255, choices=CanadianProvinces.choices)
    post_code = models.CharField(max_length=10)
    country = models.CharField(max_length=10, default="Canada")

    class Meta:
        verbose_name_plural = "addresses"


class Property(models.Model):
    mls = models.CharField(primary_key=True, max_length=10)
    monthly_rent = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    square_footage = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    title = models.CharField(max_length=20, choices=PropertyTitleTypes.choices)
    amenities = models.JSONField()
    address = models.ForeignKey(to=Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "properties"
