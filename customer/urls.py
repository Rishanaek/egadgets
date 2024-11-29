from django.urls import path
from .views import *

urlpatterns=[
    path('chome',CustomerHomeView.as_view(),name='home'),
    path('list<str:cat>',ProductlistView.as_view(),name='list'),
    path('details/<int:id>',ProductDetailView.as_view(),name='details'),
    path('cart/<int:id>',addToCart,name='cart'),
    path('cartlist',CartListView.as_view(),name='cartlist'),
    path('inc/<int:id>',IncreaseQuantity,name='inc'),
    path('dec/<int:id>',DecreaseQuantity,name='dec'),
    path('delete/<int:id>',DeleteCartItem,name='delete'),
    path('order/<int:id>',OrderPlaced,name='order'),
    path('orderlist',OrderListView.as_view(),name='orderlist'),
    path('cancelorder',cancelOrder,name='cancelorder'),
    path('search',searchproduct,name='search')
]