from django.urls import path
from . import views
from app.views import home_list, PropertyDetailView, deletes

urlpatterns = [
    path('', home_list, name='home_list'),
    path('about/', views.about, name='about'),
    path('agent/', views.agent, name='agent'),
    path('properties/', views.properties, name='properties'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search_products, name='products'),
    path('post/', views.post, name='post'),
    path('details/<int:pk>', views.details, name='details'),
    path('property/new/<int:pk>', PropertyDetailView.as_view(), name='property_new'),
    path('property/<int:pk>', PropertyDetailView.as_view(), name='property_detail'),
    path('property/', PropertyDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', deletes, name='delete'),
    path('ru-RU/', views.set_language, name='ru-RU'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('send/', views.send_mails, name='send_mails'),
    path('featured/', views.featured, name='featured'),
]
