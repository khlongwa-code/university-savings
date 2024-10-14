from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Budget

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Username'
            }
        ) 
    )

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Password'
            }
        )
    )


class RegistrationForm(UserCreationForm):
    
    username = forms.CharField(
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Username'
            }
        ) 
    )

    email = forms.EmailField(
        max_length=60,
        required=True,
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )

    password1 = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Password'
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Password'
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class BudgetForm(forms.ModelForm):
    total_income = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'income...',
                'class': 'budget-form'  # You can add CSS classes if needed
            }
        )
    )

    total_expenses = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'expenses...',
                'class': 'budget-form'
            }
        )
    )

    savings_goal = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'savings...',
                'class': 'budget-form'
            }
        )
    )

    class Meta:
        model = Budget
        fields = ('total_income', 'total_expenses', 'savings_goal')