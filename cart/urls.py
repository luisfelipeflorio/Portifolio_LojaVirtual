from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartDetailView.as_view(), name='detail'),
    path('add/', views.CartAddView.as_view(), name='add'),
    path('add/ajax/', views.CartAddAjaxView.as_view(), name='add_ajax'),
    path('remove/', views.CartRemoveView.as_view(), name='remove'),
    path('update/', views.CartUpdateView.as_view(), name='update'),
]