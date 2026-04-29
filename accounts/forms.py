from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Address

_TW_INPUT = (
    'w-full px-4 py-3 rounded-xl border border-neutral-200 bg-white '
    'focus:outline-none focus:ring-2 focus:ring-rose-400 focus:border-transparent '
    'placeholder-neutral-400 text-neutral-800 transition-all duration-200'
)


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
            field.widget.attrs.update({'class': _TW_INPUT})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': _TW_INPUT})


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
            field.widget.attrs.update({'class': _TW_INPUT})


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street', 'number', 'complement', 'neighborhood', 'city', 'state', 'zip_code', 'is_default')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'is_default':
                field.widget.attrs.update({
                    'class': 'h-4 w-4 text-rose-500 border-neutral-300 rounded cursor-pointer'
                })
            else:
                field.widget.attrs.update({'class': _TW_INPUT})
        self.fields['state'].widget.attrs['placeholder'] = 'SP'
        self.fields['zip_code'].widget.attrs['placeholder'] = '00000-000'
