from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from cart.models import Cart
from user.forms import LoginForm, RegisterForm
from user.models import CustomerUser

# Create your views here.


class AuthLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        formContent = LoginForm()
        return render(request, 'auth_page/login.html', {'formContent': formContent})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

        messages.error(request, 'Username or password is incorrect')
        return redirect('auth_login')


class AuthRegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = RegisterForm()
        return render(request, 'auth_page/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']

            try:
                is_user_existed = User.objects.get(username=username)
                messages.error(request, 'Username đã được sử dụng')
                return redirect('auth_register')
            except User.DoesNotExist:
                customer_user = CustomerUser.objects.create(user=User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                ))
                Cart.objects.create(user=customer_user)

                messages.success(request, 'Tạo tài khoản thành công')
                return redirect('auth_register')

        messages.error(request, form.errors)
        return redirect('auth_register')


def logout_view(request):
    logout(request)
    return redirect('home')


class UserProfileView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated == True:
            customer_user = CustomerUser.objects.get(user=user)
            user.customer_user = customer_user
            return render(request, 'user_page/profile.html')

        return redirect('auth_login')
