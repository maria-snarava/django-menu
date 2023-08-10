from django.db import models

# An inventory of different Ingredients, their available quantity, and their prices per unit
class Ingredient(models.Model):
    pass

#A list of the restaurant’s MenuItems, and the price set for each entry
class MenuItem(models.Model):
    pass

#A list of the ingredients that each menu item requires (RecipeRequirements)
class RecipeRequirement(models.Model):
    pass

#A log of all Purchases made at the restaurant
class Purchase(models.Model):
    pass