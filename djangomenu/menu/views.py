from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# What is currently in the restaurant’s inventory?
# What purchases have been made?
# What does the restaurant’s menu look like? What ingredients (and how many of each) are required for each item on the menu? What’s the price of each item?
# What is the total revenue for the restaurant’s overall recorded purchases?
# What is the total cost to the restaurant’s overall purchases made (sum of cost of all ingredients used).
# How much profit (revenue - cost) does the restaurant make?

def home(request):
  context = {"name": request.user, "page_title": "Home page"}

  return render(request, "menu/home.html", context)

class MenuItemList(LoginRequiredMixin, ListView):
  model = MenuItem
  template_name = "menu/items_list.html"

class MenuItemCreate(LoginRequiredMixin, CreateView):
  model = MenuItem
  template_name = "menu/item_create_form.html"
  fields = ["name", "price"]

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
  model = MenuItem
  template_name = "menu/item_update_form.html"
  fields = ["name", "price"]

class MenuItemDelete(LoginRequiredMixin, DeleteView):
  model = MenuItem
  template_name = "menu/item_delete_form.html"


class IngredientList(LoginRequiredMixin, ListView):
  model = Ingredient
  template_name = "menu/ingredient_list.html"

class IngredientCreate(LoginRequiredMixin, CreateView):
  model = Ingredient
  template_name = "menu/item_create_form.html"
  fields = ["name", "quantity", "unit", "unit_price"]


class IngredientUpdate(LoginRequiredMixin, UpdateView):
  model = Ingredient
  template_name = "menu/item_update_form.html"
  fields = ["name", "quantity", "unit", "unit_price"]

class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  template_name = "menu/item_delete_form.html"


class RecipeRequirementList(LoginRequiredMixin, ListView):
  model = RecipeRequirement
  template_name = "menu/recipe_requirement_list.html"

class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "menu/item_create_form.html"
    fields = ["menuItem", "ingredient", "quantity"]

class RecipeRequirementUpdate(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = "menu/item_update_form.html"
    fields = ["menuItem", "ingredient", "quantity"]

class RecipeRequirementDelete(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = "menu/item_delete_form.html"

class PurchaseList(LoginRequiredMixin, ListView):
  model = Purchase
  template_name = "menu/purchase_list.html"

class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "menu/item_create_form.html"
    fields = ["menuItem"]
