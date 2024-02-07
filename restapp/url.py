
from django.urls import path
from .views import ItemListCreate, Itemview, Itemdelete, Itemchange

urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list'),
    path('view/', Itemview.as_view(), name='item-get'),
    path('items/<int:pk>/delete/', Itemdelete.as_view(), name='item-get'),
    path('items/<int:pk>/update/', Itemchange.as_view(), name='yourmodel-update'),
]

