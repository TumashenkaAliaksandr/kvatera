from django.shortcuts import render


def index(request):

    return render(request, 'webapp/index-3.html')

def about(request):

    return render(request, 'webapp/about.html')
