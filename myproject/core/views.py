from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


@login_required
def index(request):
    template_name = 'index.html'
    return render(request, template_name)
