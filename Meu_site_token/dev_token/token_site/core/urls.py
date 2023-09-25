from django.urls import path
from . import views

urlpatterns = [
    path('', views.Registration, name='index'),
    path('verify/<str:token>', views.verify, name='verify')
]
