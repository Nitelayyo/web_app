from django.shortcuts import render, redirect, HttpResponse
from .models import FileUpLoad
from .do import deserialize


def upload(request):
    if request.method == 'POST':
        file2 = request.FILES['file']
        document = FileUpLoad.objects.create(file=file2)
        document.save()
        document.file.name = deserialize(document.file.path)
        return render(request, 'fileupload/download.html', {'correct': True, 'file_object': document})
    return render(request, 'fileupload/upload.html')


def download(request, path):
    # Хм, я можу підключити сюди через імпорт певну свою бібліотеку і вона все порішає
    # Тобто тоді тільки файл передам до проги і все.
    return render(request, 'fileupload/download.html')
