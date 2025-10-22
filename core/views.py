from django.shortcuts import render,redirect
from .models import Expense
from .forms import ExpenseForm
from django.contrib import messages
# Create your views here.

def index(request):
    expenses = Expense.objects.all()
    sum = 0
    count = 0
    
    for expense in expenses:
        sum += expense.amount
        count+=1
        
        context = {
            "jami_miqdori" : sum,
            "jami_soni" : count,
            "expenses" : expenses
        }
        
    return render(request,"core/index.html",context)

def add_expenses(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            print("is valid ekan ")
            form.save()
            messages.add_message(request, messages.SUCCESS,"xarajat qoshildi ")
        else:
            print("valid emas ekan ")
    
    return redirect("index")
    