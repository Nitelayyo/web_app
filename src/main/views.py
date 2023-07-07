from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {'title': 'Головна!'})


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    data = {
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/contact.html', data)
