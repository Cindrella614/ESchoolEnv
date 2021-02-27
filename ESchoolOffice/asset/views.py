from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Asset, Merchant


def asset(request):
    model_object = Asset.objects.all()
    if request.method == 'POST':
        form = forms.AssetForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("asset:AssetForms")
    else:
        form = forms.AssetForms()
    return render(request, 'asset/Asset.html', {'form': form, 'data': model_object})


def merchant(request):
    model_object = Merchant.objects.all()
    if request.method == 'POST':
        form = forms.MerchantForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("asset:MerchantForms")
    else:
        form = forms.MerchantForms()
    return render(request, 'asset/Merchant.html', {'form': form, 'data': model_object})


def delete_asset(request, pk):
    post = get_object_or_404(Asset, pk=pk)
    post.delete()
    return redirect('asset:AssetForms')


def edit_asset(request, pk):
    template = "asset/asset.html"
    post = get_object_or_404(Asset, pk=pk)
    model_object = Asset.objects.all()
    if request.method == 'POST':
        form = forms.AssetForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('asset:AssetForms')
    else:
        form = forms.AssetForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)
