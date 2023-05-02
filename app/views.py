from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .models import Home
from .models import Home


def home_list(request):
    query = request.GET.get('products')
    if query:
        homes = Home.objects.filter(name__icontains=query)
    else:
        homes = Home.objects.all()
    context = {
        "homes": homes
    }
    return render(request=request, template_name='index.html', context=context)


def about(request):
    context = {
        'content': 'This website to sell Houses',
    }
    return render(request, 'files/about.html', context)


def agent(request):
    context = {
        'agent': 'Our agent Amir',
    }
    return render(request, 'files/agent.html', context)


def services(request):
    context = {
        'services': 'Services',
    }
    return render(request, 'files/services.html', context)


def properties(request):
    context = {
        'properties': 'Properties',
    }
    return render(request, 'files/properties.html', context)


def blog(request):
    context = {
        'blog': 'Blog',
    }
    return render(request, 'files/blog.html', context)


def contact(request):
    context = {
        'contact': 'Contact',
    }
    return render(request, 'files/contact.html', context)


# def login(request):
#     context = {
#         'login': 'Login',
#     }
#     return render(request, 'files/login.html', context)
#
#
# def register(request):
#     context = {
#         'register': 'Register',
#     }
#     return render(request, 'files/register.html', context)

from django.contrib.auth import authenticate, login as auth_login


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password, first_name=name, last_name=surname)
        user.save()
        return redirect('login')
    else:
        return render(request, 'files/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
    return render(request, 'files/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def search_products(request):
    query = request.GET.get('products')
    if query:
        products = Home.objects.filter(name__icontains=query)
    else:
        products = Home.objects.all()
    context = {'products': products, 'query': query}
    return render(request, 'files/search_results.html', context)
