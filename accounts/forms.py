from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='nome', max_length=30, required=True)
    last_name = forms.CharField(label='sobrenome', max_length=30, required=True)
    email = forms.EmailField(label='e-mail', required=True)
    phone = forms.CharField(label='telefone', max_length=20, required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-3 rounded-xl border border-neutral-200 bg-white focus:outline-none focus:ring-2 focus:ring-rose-400 focus:border-transparent placeholder-neutral-400 text-neutral-800 transition-all duration-200'
            })


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-3 rounded-xl border border-neutral-200 bg-white focus:outline-none focus:ring-2 focus:ring-rose-400 focus:border-transparent placeholder-neutral-400 text-neutral-800 transition-all duration-200'
            })


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='nome', max_length=30, required=True)
    last_name = forms.CharField(label='sobrenome', max_length=30, required=True)
    phone = forms.CharField(label='telefone', max_length=20, required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-3 rounded-xl border border-neutral-200 bg-white focus:outline-none focus:ring-2 focus:ring-rose-400 focus:border-transparent placeholder-neutral-400 text-neutral-800 transition-all duration-200'
            })
