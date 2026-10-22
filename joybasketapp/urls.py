from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home),
    path('starter/', views.starter, name='starter'),
    path('services/', views.service_details, name='service_details'),
    path('portfolio/', views.portfolio_details, name='portfolio_details'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('show/', views.show, name='show'),
]