from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_baby(request):
    return HttpResponse("Hello, worldz. You're at the polls index.")

def hit_me_baby_one_more_time(request):
    return HttpResponse("It's Britney bish.")