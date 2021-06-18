from django.urls import path
from TFS import views

urlpatterns = [
    path('',views.Home),
    path('home',views.Home),
    path('customers',views.customers),
    path('trans',views.trans),
]