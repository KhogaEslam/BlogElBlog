from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import category
from forms import category_form


# Create your views here.
def showCategory(request):
    allCategory = category.objects.all()
    context = {'allCategory': allCategory}
    return render(request, 'adminpanel/category/index.html', context)


# add
def add_category(request):
    form = category_form()
    if request.method == 'POST':
        form = category_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adminpanal/all')

    context = {'cat_form': form}
    return render(request, 'adminpanel/category_form.html', context)


# edit
def edit_category(request, id):
    cat = category.objects.get(id=id)
    form = category_form(instance=cat)
    if request.method == 'POST':
        form = category_form(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adminpanel/all')

    context = {'cat_form': form}
    return render(request, 'adminpanel/category_form.html', context)


# delete
def del_category(request, id):
    cat = category.objects.get(id=id)
    cat.delete()
    return HttpResponseRedirect('/adminpanel/all')
