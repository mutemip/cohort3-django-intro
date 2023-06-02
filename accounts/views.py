from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Our Login View
def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username') # viny
            password = request.POST.get('password') # viny@123!
            user = authenticate(request, username=username, password=password)
            #TRUE/FASLE

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'username or password is incorrect!') 
        return render(request, 'login.html')

# Our register view
def register_View(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # save passed data
            login(request, user) # login the user
            messages.success(request, "Registration Successful")
            return redirect("/")
        messages.error(request, "Invalid information")
        
    context = {
        "register_form": form,
    }
        
    return render(request, "register.html", context)


def user_logout(request):
    logout(request)
    return redirect('/')