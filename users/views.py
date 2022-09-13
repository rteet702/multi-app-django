from django.shortcuts import HttpResponse, redirect


# Create your views here.
def root(request):
    return redirect('/blogs')


def index(request):
    return HttpResponse('Placeholder to later display all the users.')


def login(request):
    return HttpResponse('Placeholder for users to login.')


def register(request):
    return HttpResponse('Placeholder for users to register.')