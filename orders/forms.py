from django import forms


class CheckoutForm(forms.Form):
    customer_name = forms.CharField(
        label='Nome completo',
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-neutral-200 bg-white focus:outline-none focus:ring-2 focus:ring-rose-400 focus:border-transparent placeholder-neutral-400 text-neutral-800 transition-all duration-200',
            'placeholder': 'Seu nome completo'
        })
    )
    customer_email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-neutral-200 bg-white focus:outline-none focus:ring-2 focus:ring-rose-400 focus:border-transparent placeholder-neutral-400 text-neutral-800 transition-all duration-200',
            'placeholder': 'seu@email.com'
        })
    )
    customer_phone = forms.CharField(
        label='Telefone',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-neutral-200 bg-white focus:outline-none focus:ring-2 focus:ring-rose-400 focus:border-transparent placeholder-neutral-400 text-neutral-800 transition-all duration-200',
            'placeholder': '(11) 99999-9999'
        })
    )
    delivery_type = forms.ChoiceField(
        label='Tipo de entrega',
        choices=[('pickup', 'Retirada na loja'), ('delivery', 'Entrega')],
        widget=forms.RadioSelect(attrs={
            'class': 'flex gap-4'
        })
    )
    delivery_address = forms.CharField(
        label='Endereço de entrega',
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-neutral-200 bg-white focus:outline-none focus:ring-2 focus:ring-rose-400 focus:border-transparent placeholder-neutral-400 text-neutral-800 transition-all duration-200',
            'placeholder': 'Rua, número, complemento, bairro, cidade, estado',
            'rows': 3
        }),
        required=False
    )
    scheduled_at = forms.DateTimeField(
        label='Data/hora agendada',
        widget=forms.DateTimeInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-neutral-200 bg-white focus:outline-none focus:ring-2 focus:ring-rose-400 focus:border-transparent text-neutral-800 transition-all duration-200',
            'type': 'datetime-local'
        }),
        required=False
    )
    notes = forms.CharField(
        label='Observações',
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-neutral-200 bg-white focus:outline-none focus:ring-2 focus:ring-rose-400 focus:border-transparent placeholder-neutral-400 text-neutral-800 transition-all duration-200',
            'placeholder': 'Alguma observação especial para o pedido?',
            'rows': 3
        }),
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        delivery_type = cleaned_data.get('delivery_type')
        delivery_address = cleaned_data.get('delivery_address')

        if delivery_type == 'delivery' and not delivery_address:
            self.add_error('delivery_address', 'Endereço de entrega é obrigatório para entrega.')

        return cleaned_data