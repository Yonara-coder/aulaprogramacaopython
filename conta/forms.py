from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput,
        min_length=8,
        help_text='A senha deve ter pelo menos 8 caracteres.'
    )
    password2 = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User 
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas não são iguais!')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user