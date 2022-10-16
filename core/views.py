from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, auth


class IndexView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(
                request, 'Invalid!!, Check your username or password.')
            return redirect('/')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, "Your account has been created! Your are now able to login.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "signup.html", {'form': form})