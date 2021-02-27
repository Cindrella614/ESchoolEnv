from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import *


def create(request):
    if request.method == 'POST':
        print("we are here")
        form = PTADesignationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved")
    else:
        form = PTADesignationForm()
        return render(request, 'pta\PTADesignation.html', {'form': form})


class PTADesignationIndexView(generic.ListView):
    template_name = 'pta\PTADesignationIndex.html'
    context_object_name = 'pta_designation_list'

    def get_queryset(self):
        abcd = PTADesignation.objects.all()
        print(abcd)
        return abcd


class PTADesignationDetailView(generic.DetailView):
    model = PTADesignation
    template_name = 'pta/PTADesignationView.html'
