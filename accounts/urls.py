from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('addresses/', views.AddressListView.as_view(), name='address_list'),
    path('addresses/create/', views.AddressCreateView.as_view(), name='address_create'),
    path('addresses/update/<int:pk>/', views.AddressUpdateView.as_view(), name='address_update'),
    path('addresses/delete/<int:pk>/', views.AddressDeleteView.as_view(), name='address_delete'),
    path('addresses/set-default/<int:pk>/', views.AddressSetDefaultView.as_view(), name='address_set_default'),
]
