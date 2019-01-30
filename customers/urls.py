from django.urls import path

from customers import views

urlpatterns = [
    path(
        '',
        views.CustomerListView.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='list-customers'
    )
]
