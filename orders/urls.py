from django.urls import path

from orders import views

urlpatterns = [
    path(
        '',
        views.OrderCreateListView.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='list-orders'
    ),

    path(
        '<int:pk>',
        views.OrderRetrieveView.as_view({
            'get': 'retrieve'
        }),
        name='retrieve-order'
    ),

    path(
        '<int:pk>/status',
        views.OrderRetrieveStatusView.as_view({
            'get': 'retrieve'
        }),
        name='retrieve-order-status'
    ),

    path(
        'detail/<int:pk>',
        views.OrderDetailsUpdateView.as_view({
            'put': 'update'
        }),
        name='update-order-details'
    ),
]
