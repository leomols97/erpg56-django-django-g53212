from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse # <- old

from .models import Developer  # <- new
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    # return HttpResponse("Hello, world. You're at the developers index.") # <- old
    context = {  # <- new
        'developers': Developer.objects.all()  # <- new
    }  # <- new
    return render(request, 'developer/index.html', context)  # <-new


def detail(request, developer_id):  # <- new
    developer = get_object_or_404(Developer, pk=developer_id)  # <- new
    return render(request, 'developer/detail.html', {'developer': developer})

def create(request):
    Developer.objects.create(
        first_name=request.POST['first_name'],
        last_name = request.POST['last_name']
    )
    # Toujours renvoyer une HTTPResponseRedirect après avoir géré correctement
    # les données de la requête POST. Cela empêche les données d'être postée deux
    # fois si l'utilisateur clique sur le bouton précédent.
    return HttpResponseRedirect(reverse('developer:index'))