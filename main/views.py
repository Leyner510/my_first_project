from main.models import Person
from django.http import Http404
from django.shortcuts import render, get_object_or_404

def index(request):
    person = Person.objects.all()
    return render(request, 'main/index.html', {'name':'Главная страница сайта','person':person})

def person_list(request):
    return render(request, 'main/person.html')




