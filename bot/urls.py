from django.urls import path
from . import views

urlpatterns = [
     path('', views.home_view, name='home'),
     path('sendurl/<str:url>/', views.send_url, name='send_url'),
     path('bot/', views.bot_view, name='bot')
]


