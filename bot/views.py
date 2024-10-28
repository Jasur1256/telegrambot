from django.shortcuts import render
from django.core.management.base import BaseCommand
from django.conf import settings 
from django.http import HttpResponse


def bot_view(request):
    return render(request, 'bot.html')


def home_view(request):
    return render(request, 'home.html')


def send_url(request, url):
    return HttpResponse(f"URL: {url} qabul qilindi!")


def start(request):
    return HttpResponse("Bot ishga tushdi!")



class Command(BaseCommand):
    help = 'Telegram botini ishga tushirish'

        


