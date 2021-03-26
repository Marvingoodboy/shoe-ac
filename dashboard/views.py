import os

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .filters import ShoeFilter
from .forms import EditShoeForm
from .models import Shoe


# Dashboard page view
@login_required(login_url='login')
def dashboard_page(request):
    shoes = Shoe.objects.all()
    shoes_filter = ShoeFilter(request.GET, queryset=shoes)
    shoes = shoes_filter.qs
    return render(request, 'home.html', {'shoes': shoes, 'shoes_filter': shoes_filter})


# Shoe page view
@login_required(login_url='login')
def view_shoe(request, pk):
    shoe = get_object_by_pk(Shoe, pk)
    return render(request, 'shoe_view.html', {'shoe': shoe})


# Edit shoe page view
@login_required(login_url='login')
def edit_shoe(request, pk):
    shoe = get_object_by_pk(Shoe, pk)
    if request.method == 'POST':
        old_image = shoe.image.path
        form = EditShoeForm(request.POST, request.FILES, instance=shoe)
        if form.is_valid():
            form.save()
        if os.path.isfile(old_image) and len(request.FILES) != 0:
            os.remove(old_image)
        return redirect('dashboard')
    form = EditShoeForm(instance=shoe)
    return render(request, 'shoe_edit.html', {'form': form, 'shoe': shoe})


# Delete shoe view
@login_required(login_url='login')
def delete_shoe(request, pk):
    shoe = get_object_by_pk(Shoe, pk)
    shoe.delete()
    return redirect('dashboard')


# Get shoe by pk
def get_object_by_pk(cls, pk):
    return cls.objects.get(pk=pk)
