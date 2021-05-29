from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requests, nome, idade):
    return HttpResponse('<pre>Hello World, {}, vc tem {} anos? </pre>'.format(nome, idade))