from django.shortcuts import render
from django.http import HttpResponse
from random import sample

def show_index(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian'
    ]
    selected_fruits = sample(fruits, 3)
    return render(request, 'index.html', {'fruits': selected_fruits})
