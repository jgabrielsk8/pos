from django.urls import path

from pizzas import views

urlpatterns = [
    path('', views.PizzaListView.as_view(), name='list-pizzas')
]
