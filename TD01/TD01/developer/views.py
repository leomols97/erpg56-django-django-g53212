from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView  # <- On ajoute ListView

from developer.templates.developer.forms import DeveloperForm
from .models import Developer  # <- new


# from django.http import HttpResponse # <- old


def index(request):
    # return HttpResponse("Hello, world. You're at the developers index.") # <- old
    context = {  # <- new
        'developers': Developer.objects.all(),
        'form': DeveloperForm,
    }
    return render(request, 'developer/index.html', context)  # <-new


def create(request):
    form = DeveloperForm(request.POST)
    if form.is_valid():
        Developer.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )
    # Toujours renvoyer une HTTPResponseRedirect après avoir géré correctement
    # les données de la requête POST. Cela empêche les données d'être postée deux
    # fois si l'utilisateur clique sur le bouton précédent.
    return HttpResponseRedirect(reverse('developer:index'))


class DevDetailVue(DetailView):
    model = Developer
    template_name = 'developer/detail.html'
    # def detail(request, developer_id):
    #     developer = Developer.objects.get(pk=developer_id)
    #     developer = get_object_or_404(Developer, pk=developer_id)
    #     return render(request, 'developer/detail.html', {'developer': developer})


class IndexView(ListView):  # <- new
    model = Developer  # <- new
    template_name = "developer/index.html"  # <- new
    context_object_name = 'developers'  # <- new

    def get_context_data(self, **kwargs):  # <- new
        context = super(IndexView, self).get_context_data(**kwargs)  # <- new
        context['form'] = DeveloperForm  # <- new
        return context  # <- new
