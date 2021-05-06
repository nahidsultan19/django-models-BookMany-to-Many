from django.shortcuts import render
from django.http import HttpResponse


def bookview(request):
    return HttpResponse('Hello Django!')
