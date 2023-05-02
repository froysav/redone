from django.urls import path
from . import views
from app.views import home_list

urlpatterns = [
    path('', home_list, name='home_list'),
    path('about/', views.about, name='about'),
    path('agent/', views.agent, name='agent'),
    path('services/', views.services, name='services'),
    path('properties/', views.properties, name='properties'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search_products, name='products'),
]
