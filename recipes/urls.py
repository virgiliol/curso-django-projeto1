from django.urls import path

from recipes import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name="home"),  # home
    path('recipes/category/<int:category_id>/', views.category, name="category"),   #recipe
    path('recipes/<int:id>/', views.recipe, name="recipe"),   #recipe
    
]