from django.db import models
from django.urls import reverse


class Item(models.Model):
    entry_dateTime = models.DateTimeField(
        verbose_name="DateTime of Entry of item into Database", auto_now_add=True
    )
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_can_be_seen = models.BooleanField(
        verbose_name="Determines if the item can be seen by the customer"
    )
    item_profit_percentage = models.FloatField(
        verbose_name="Profit margin percentage made on the item"
    )

    class typeOfItems(models.TextChoices):
        grocery = "Grocery"
        consumables = "Consumables"
        frozen = "Frozen Food"
        toys = "Toys"
        other = "Others"

    item_type = models.CharField(max_length=20,choices=typeOfItems.choices)
    
    item_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("merchant:detail", kwargs={"pk": self.pk})
