from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartDetailView.as_view(), name='detail'),
    path('add/', views.CartAddView.as_view(), name='add'),
    path('remove/<int:product_id>/', views.CartRemoveView.as_view(), name='remove'),
    path('update/<int:product_id>/', views.CartUpdateView.as_view(), name='update'),
]