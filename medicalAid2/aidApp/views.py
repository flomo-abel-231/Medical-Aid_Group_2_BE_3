from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required




def home (request):

    return render(request, "base.html")


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.error)

    else:
        user_form = UserForm
        profile_form = UserProfileForm

    return render(request, 'aidApp/registration.html',
                  {"registered": registered,
                   "user_form": user_form,
                   "profile_form": profile_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse(" ACCOUNT IS DEACTIVATED ")
        else:
            return HttpResponse(" Please use a correct user id and password ")

    else:
        return render(request, 'aidApp/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("Home"))

