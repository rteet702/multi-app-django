from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Placeholder to display all the surveys created.')


def new(request):
    return HttpResponse('Placeholder for users to add a new survey.')