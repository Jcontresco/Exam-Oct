import re
from django.shortcuts import redirect, render
from .forms import UserForm
# Create your views here.
def login(request):
 
    context = {
        'userForm': UserForm()
    }
    return render(request, 'register.html', context=context)


def createUser(request):
    # POST 
    if request.method == 'POST':
        formResults = UserForm(request.POST)
        if formResults.is_valid():
            return redirect('/')
        context = {
            'userForm': formResults,
            # 'formErrors': UserForm().errors
        }
        return render(request, 'register.html', context=context)