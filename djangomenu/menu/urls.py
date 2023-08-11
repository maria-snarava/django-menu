from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="homePage"),
    path("ingredient/list", views.IngredientList.as_view(), name="ingredient_list"),
    path("ingredient/create", views.IngredientCreate.as_view(), name="ingredient_create"),
    path("ingredient/update/<pk>", views.IngredientUpdate.as_view(), name="ingredient_update"),
    path("ingredient/delete/<pk>", views.IngredientDelete.as_view(), name="ingredient_delete"),

    path("menuItem/list", views.MenuItemList.as_view(), name="menu_item_list"),
    path("menuItem/create", views.MenuItemCreate.as_view(), name="menu_item_create"),
    path("menuItem/update/<pk>", views.MenuItemUpdate.as_view(), name="menu_item_update"),
    path("menuItem/delete/<pk>", views.MenuItemDelete.as_view(), name="menu_item_delete"),

    path("recipeRequirement/list", views.RecipeRequirementList.as_view(), name="recipe_requirement_list"),
    path("recipeRequirement/create", views.RecipeRequirementCreate.as_view(), name="recipe_requirement_create"),
    path("recipeRequirement/update/<pk>", views.RecipeRequirementUpdate.as_view(), name="recipe_requirement_update"),
    path("recipeRequirement/delete/<pk>", views.RecipeRequirementDelete.as_view(), name="recipe_requirement_delete"),

    path("purchase/list", views.PurchaseList.as_view(), name="purchase_list"),
    path("purchase/create", views.PurchaseCreate.as_view(), name="purchase_create"),

    path("login/", include("django.contrib.auth.urls"), name="login"),
    path("analytics/", views.analytics, name="analytics"),
    path('logout/', views.logout_view, name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
]