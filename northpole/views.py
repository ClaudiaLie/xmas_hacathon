from django.shortcuts import render


def index(request):
    """ A view to return index page """

    return render(request, 'northpole/index.html')