from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('puranpatra/', views.puranpatra, name='puranpatra'),
    path('sinhasan/', views.sinhasan, name='sinhasan'),

]