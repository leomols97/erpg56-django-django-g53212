from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse # <- old

from .models import Developer  # <- new


def index(request):
    # return HttpResponse("Hello, world. You're at the developers index.") # <- old
    context = {  # <- new
        'developers': Developer.objects.all()  # <- new
    }  # <- new
    return render(request, 'developer/index.html', context)  # <-new


def detail(request, developer_id):  # <- new
    developer = get_object_or_404(Developer, pk=developer_id)  # <- new
    return render(request, 'developer/detail.html', {'developer': developer})
