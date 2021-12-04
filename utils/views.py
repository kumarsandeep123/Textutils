
# views.py
# I have created this file -Sandeep kumar
from django.http import HttpResponse
from django.shortcuts import render


def san(request):
    return render(request, 'san.html')

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')





def analyze(request):
    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    punctuations = '''!()-[]`{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for character in djtext:
        if character not in punctuations:
            analyzed = analyzed + character
    params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
    return render(request,'analyze.html',params)