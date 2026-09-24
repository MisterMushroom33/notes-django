from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect

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
    # Читаем тему оформления из cookies, если её нет - используем 'light' по умолчанию
    current_theme = request.COOKIES.get('theme', 'light')
    return render(request, 'notes/notes_list.html', {
        'notes': notes_data,
        'current_theme': current_theme,
    })

def add_note(request):
    if request.method == 'POST':
        # Забираем данные из формы
        new_id = len(notes_data) + 1
        title = request.POST.get('title')
        text = request.POST.get('text')
        theme = request.POST.get('theme', 'light')

        notes_data.append({
            'id': new_id,
            'title': title,
            'text': text,
            'theme': theme,
        })
        return redirect('notes_list')

    current_theme = request.COOKIES.get('theme', 'light')
    return render(request, 'notes/add_note.html', {'current_theme': current_theme})

def set_theme(request, theme_name):
    # Сохраняем выбор темы в cookies и возвращаем на главную
    response = redirect('notes_list')
    response.set_cookie('theme', theme_name, max_age=30*24*60*60)  # хранится 30 дней
    return response