from audioop import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.timezone import activate
from django.views import View
from .forms import RentalForm
from .models import Home, Happys, Cities, Agent, Blog


def home_list(request):
    query = request.GET.get('products')
    if query:
        homes = Home.objects.filter(name__icontains=query)
    else:
        homes = Home.objects.all()
    homese = Happys.objects.all()
    city = Cities.objects.all()
    agent = Agent.objects.all()
    blog = Blog.objects.all()
    context = {
        "homes": homes,
        'homese': homese,
        "city": city,
        "agent": agent,
        "blog": blog,
    }
    return render(request=request, template_name='index.html', context=context)


def about(request):
    city = Cities.objects.all()
    context = {
        'city': city,
    }
    return render(request, 'files/about.html', context)


def agent(request):
    agent = Agent.objects.all()
    context = {
        'agent': agent,
    }
    return render(request, 'files/agent.html', context)


def properties(request):
    homes = Home.objects.all()
    context = {
        'homes': homes,
    }
    return render(request, 'files/properties.html', context)


def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog,
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


def post(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        picture = request.POST.get('picture')
        rental_period = request.POST.get('rental_period')
        taking_time = request.POST.get('taking_time')
        sqft = request.POST.get('sqft')
        name = request.POST.get('name')
        place = request.POST.get('place')
        owner = request.POST.get('owner')
        upload_time = request.POST.get('upload_time')
        product = Home.objects.create(
            price=price,
            picture=picture,
            rental_period=rental_period,
            taking_time=taking_time,
            sqft=sqft,
            name=name,
            place=place,
            owner=owner,
            upload_time=upload_time
        )
        product.save()
        return redirect('/')
    return render(request, 'detail.html')


def details(request, pk):
    item = Home.objects.get(pk=pk)
    context = {
        'item': item,
    }
    return render(request, 'files/details.html', context)




class PropertyDetailView(View):
    def get(self, request, pk):
        form = RentalForm()
        return render(request, 'files/update.html', {'form': form})

    def posts(self, request, pk):
        form = RentalForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save()
            return redirect('home_list')
        else:
            return render(request, 'files/update.html', {'form': form})


def deletes(request, pk):
    record = Home.objects.get(pk=pk)
    record.delete()
    return redirect('home_list')


def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language', None)
        if language:
            request.session[Home] = language
            activate(language)
        else:
            pass
    return redirect('/')


def forgot_password(request):
    context = {
        'forgot_password': 'forgot_password',
    }
    return render(request, 'files/password.html', context)


def send_mails(request):
    context = {
        'send_mail': 'Send_mail',
    }
    send_mail(
        'Hello go to this link',
        'http://127.0.0.1:8000/register/',
        'roncrist5575@gmail.com',
        ['roncrist5575@gmail.com'],
        fail_silently=False,
    )
    return render(request, 'files/register.html', context)


def featured(request):
    context = {
        'featured': 'Featured',
    }
    return render(request, 'files/featured.html', context)
