from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    """
    This view asks new users to sign up
    """
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})