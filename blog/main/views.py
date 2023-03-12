from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    params = {'page_title': 'ГЛАВНА СТРАНИЦА',
              'page_header': 'Главна страница',
              'page_content': 'Текст на страницата',
              }
    return render(request, 'main/index.html', params)


def all_articles(request):
    params = {'page_title': 'Всички публикации',
              'page_header': 'Всички публикации',
              'page_content': 'Пълен списък на всички публикации',
              }
    return render(request, 'main/index.html', params)