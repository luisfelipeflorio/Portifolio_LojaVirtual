from django.views.generic import CreateView, FormView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('core:home')


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('core:home')


class LogoutView(FormView):
    def get(self, request):
        from django.contrib.auth import logout
        logout(request)
        return redirect('core:home')


class ProfileView(UpdateView):
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')