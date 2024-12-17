from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from products.models import Basket


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()

    user_messages = messages.get_messages(request)
    context = {
        'form': form,
        'messages': user_messages,
    }
    return render(request, 'users/register.html', context=context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Вы успешно вошли в систему')
                return HttpResponseRedirect(reverse('main'))
            else:
                messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = UserLoginForm()

    user_messages = messages.get_messages(request)
    context = {
        'form': form,
        'messages': user_messages,
    }
    return render(request, 'users/login.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)

    # Исправлено: вызываем метод basket.sum()
    total_sum = sum(basket.sum() for basket in baskets)
    total_quantity = sum(basket.quantity for basket in baskets)

    context = {
        'form': form,
        'baskets': baskets,
        'total_sum': total_sum,
        'total_quantity': total_quantity,
    }
    return render(request, 'users/profile.html', context=context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
