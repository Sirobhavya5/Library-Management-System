from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

from users.forms import UserSignUpForm, UserLoginForm
from users.models import CustomUser

# Create your views here.
def signup(request):
    if request.method == "POST":
        try:
            form = UserSignUpForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['password'] == form.cleaned_data['password_confirmation']:
                    user = CustomUser.objects.create_user(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'], phone_number=form.cleaned_data["phone_number"], password=form.cleaned_data['password'], role=form.cleaned_data["role"], street=form.cleaned_data["street"], city=form.cleaned_data["city"], state=form.cleaned_data["state"], zip_code=form.cleaned_data["zip_code"])
                    django_login(request, user)
                    return redirect('/')
            else:
                raise Exception(e)
        except Exception as e:
            print(e)
            return render(request, 'users/signup.html', {"form": form})
    else:
        form = UserSignUpForm()
        return render(request, 'users/signup.html', {"form": form})

def login(request):
    if request.method == "POST":
        try:
            form = UserLoginForm(request.POST)
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
                django_login(request, user)
                return redirect("/")
            else:
                raise Exception(e)
        except Exception as e:
            print(e)
            return render(request, 'users/login.html', {"form": form})
    else:
        form = UserLoginForm()
        return render(request, 'users/login.html', {"form": form})

def logout(request):
    try:
        django_logout(request)
    except Exception as e:
        print(e)
    finally:
        return redirect('/')
