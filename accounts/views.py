from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RegisterForm, ProfileForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class ProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user