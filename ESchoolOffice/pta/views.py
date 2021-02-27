from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *


def create(request):
    print("here")
    if request.method == 'POST':
        form = PTADesignationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = PTADesignationForm()
        path = 'pta\PTADesignation.html'
        return render(request, path, {'form': form})




