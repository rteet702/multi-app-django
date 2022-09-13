from django.shortcuts import HttpResponse, redirect


# blogs views.
def index(request):
    return HttpResponse('Placeholder to later display a list of all blogs.')


def new(request):
    return HttpResponse('Placeholder to display a new form to create a new blog.')


def create(request):
    return redirect('/blogs')


def show(request, id):
    return HttpResponse(f'Placeholder to display blog number: {id}')


def edit(request, id):
    return HttpResponse(f'Placeholder to edit blog number: {id}')


def destroy(request, id):
    return redirect('/blogs')