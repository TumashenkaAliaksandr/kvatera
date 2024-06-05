from django.shortcuts import render


def index(request):

    return render(request, 'webapp/index-3.html')


def about(request):

    return render(request, 'webapp/about.html')


def contacts(request):

    return render(request, 'webapp/contact.html')


def objects_rent(request):

    return render(request, 'webapp/grid-leftfilter.html')


def detail_full(request):

    return render(request, 'webapp/detail-fullwidth.html')
