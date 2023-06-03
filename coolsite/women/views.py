from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложение women.")

def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        raise Http404()

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Этой ебучей страницы нет</h1>')
