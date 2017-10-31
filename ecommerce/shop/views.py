from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.db.models import Q

from .models import Product, Order, Cart


def home(request):
    # get the 20 cheapest products by default, before user does a search
    product_list = Product.objects.order_by('price')[:20]
    context = {'product_list': product_list}
    print(product_list)
    return render(request, 'shop/base_search_page.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or username already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def view_cart(request):
    return render(request, 'shop/base_cart.html')


def view_orders(request):
    return render(request, 'shop/base_orders_page.html')


