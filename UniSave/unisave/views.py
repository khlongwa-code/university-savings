from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import LoginForm, RegistrationForm, BudgetForm
from .models import Budget, Expense

# Create your views here.

def home_view(request):
    user = request.user
    login_form = LoginForm()
    signup_form = RegistrationForm()

    context = {
            'login_form': login_form,
            'signup_form': signup_form,
            'is_authenticated': request.user.is_authenticated,
        }

    if user.is_authenticated:
        context['registered_user'] = user.first_name

    return render(request, 'base.html', context)

def signin_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return redirect('home')

def signout_view(request):
    logout(request)
    return redirect('home')

def budget_view(request):
    # Check if the user already has a budget
    try:
        budget = Budget.objects.get(user=request.user)
        has_budget = True
    except Budget.DoesNotExist:
        budget = None
        has_budget = False

    if request.method == 'POST':
        
        budget_form = BudgetForm(request.POST)
        if budget_form.is_valid():
            
            new_budget = budget_form.save(commit=False)
            new_budget.user = request.user
            new_budget.save()
            return redirect('budget')
    else:
        budget_form = BudgetForm(instance=budget) if has_budget else BudgetForm()

    return render(request, 'budget.html', {
        'budget_form': budget_form,
        'budget': budget,
        'has_budget': has_budget,
    })

def create_budget(request):
    if request.method == 'POST':
        total_income = request.POST['total_income']
        total_expenses = request.POST['total_expenses']
        savings_goal = request.POST['savings_goal']

        budget = Budget.objects.create(
            user=request.user,
            total_income=total_income,
            total_expenses=total_expenses,
            savings_goal=savings_goal
        )
        return redirect('budget')

def edit_budget(request):
    if request.method == 'POST':
        budget = Budget.objects.get(user=request.user)
        budget.total_income = request.POST['total_income']
        budget.total_expenses = request.POST['total_expenses']
        budget.savings_goal = request.POST['savings_goal']
        budget.save()
        return redirect('budget')

def delete_budget(request):
    budget = Budget.objects.get(user=request.user)
    budget.delete()
    return redirect('budget')

def expenses_view(request):
    # Retrieve expenses for the logged-in user
    try:
        expenses = Expense.objects.filter(user=request.user)
        has_expenses = expenses.exists()
    except Expense.DoesNotExist:
        expenses = None
        has_expenses = False

    return render(request, 'expenses.html', {
        'expenses': expenses,
        'has_expenses': has_expenses,
    })

def clear_expenses(request):
    if request.method == 'POST':
        
        Expense.objects.filter(user=request.user).delete()
        messages.success(request, "All expenses have been cleared.")
        return redirect('expenses')
