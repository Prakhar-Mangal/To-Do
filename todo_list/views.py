from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            #form.save()
            all_items = List.objects.filter(user=request.user)
            messages.success(request,('Item has been added to List...'))
            return render(request, 'todo_list/home.html', {'all_items':all_items})

    else:
            if not request.user.is_authenticated:
                return redirect('/')
            else:
                all_items = List.objects.filter(user=request.user)
                return render(request, 'todo_list/home.html', {'all_items':all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item has been deleted...'))
    return redirect('todo')

def done(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    messages.success(request,('Task Done'))
    return redirect('todo')

def undone(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    messages.success(request,('Task UnDone'))
    return redirect('todo')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST, instance = item)

        if form.is_valid():
            form.save()
            messages.success(request,('Item has been edited'))
            return redirect('todo')

    else:
        item = List.objects.get(pk=list_id)
        return render(request,'todo_list/edit.html', {'item':item})
        