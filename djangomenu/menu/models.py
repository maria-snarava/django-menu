from django.db import models

# An inventory of different Ingredients, their available quantity, and their prices per unit
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=30)
    unit_price = models.FloatField(default=0.0)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
      return "list"

    class Meta:
        ordering = ["name"]


#A list of the restaurant’s MenuItems, and the price set for each entry
class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return "list"
    class Meta:
        ordering = ["-price"]

#A list of the ingredients that each menu item requires (RecipeRequirements)
class RecipeRequirement(models.Model):
    menuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

    def __str__(self):
        return '{}'.format(self.menuItem)
    def get_absolute_url(self):
        return "list"

    class Meta:
        ordering = ["menuItem"]

#A log of all Purchases made at the restaurant
class Purchase(models.Model):
    menuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.menuItem)

    def get_absolute_url(self):
        return "list"

    class Meta:
        ordering = ["timestamp"]