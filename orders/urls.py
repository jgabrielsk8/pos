from django.urls import path

from orders import views

urlpatterns = [
    path(
        '',
        views.OrderListView.as_view(),
        name='list-orders'
    ),

    path(
        '<int:pk>/details',
        views.OrderDetailListView.as_view(),
        name='order-details'
    )
]
