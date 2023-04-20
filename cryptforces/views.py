from django.shortcuts import render
from django.http import HttpResponse
from cryptforces.models import CustomUser

# Create your views here.

def index(request):
    return render(request, 'index.html')


def leaderboard(request):
    user_list = CustomUser.objects.all().order_by('-points')
    return render(request, 'leaderboard.html', {'user_list': user_list})

def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})