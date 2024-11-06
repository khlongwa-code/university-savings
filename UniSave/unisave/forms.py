from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Budget, Transaction, Income, Expense

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


class TransactionForm(forms.ModelForm):
    amount = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Enter amount...',
                'class': 'transaction-form-input'
            }
        )
    )
    transaction_type = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,  # Use radio buttons
        choices=Transaction.TRANSACTION_TYPE_CHOICES
    )
    transaction_date = forms.DateTimeField(
        required=False,  # Optional, or you can make it required
        widget=forms.DateInput(
            attrs={
                'placeholder': 'Transaction date...',
                'class': 'transaction-form-input',
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type', 'transaction_date']


class IncomeForm(forms.ModelForm):
    amount = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Enter income amount...',
                'class': 'income-form-input'
            }
        )
    )
    source = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Source of income...',
                'class': 'income-form-input'
            }
        )
    )
    date_received = forms.DateTimeField(
        required=False,  # Optional field
        widget=forms.DateInput(
            attrs={
                'placeholder': 'Date received...',
                'class': 'income-form-input',
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Income
        fields = ['amount', 'source', 'date_received']


class ExpenseForm(forms.ModelForm):
    amount = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Enter income amount...',
                'class': 'income-form-input'
            }
        )
    )
    category = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Source of income...',
                'class': 'income-form-input'
            }
        )
    )
    date_spent = forms.DateTimeField(
        required=False,  # Optional field
        widget=forms.DateInput(
            attrs={
                'placeholder': 'Date received...',
                'class': 'income-form-input',
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Expense
        fields = ['amount', 'category', 'date_spent']
