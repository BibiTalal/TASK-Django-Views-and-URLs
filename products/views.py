from django.http import HttpResponse
from django.shortcuts import render


def get_home(request):
    return HttpResponse("<h1> Welcome</h1>")
