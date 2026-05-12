from django.shortcuts import render
def gTemp(response):
    return render(response, 'index.html')