from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

notes_data = [
    {
        'id': 1,
        'title': 'Первая заметка',
        'text': 'Это текст первой заметки для теста.',
        'theme': 'light',
    },
    {
        'id': 2,
        'title': 'Список покупок',
        'text': 'Молоко, хлеб, яйца, кофе.',
        'theme': 'dark',
    },
    {
        'id': 3,
        'title': 'Идея для проекта',
        'text': 'Сделать приложение для заметок с темами оформления.',
        'theme': 'blue',
    },
]

def notes_list(request):
    return render(request, 'notes/notes_list.html', {'notes': notes_data})