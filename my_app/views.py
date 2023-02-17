from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import TodoItem


def index(request):
    todos = TodoItem.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:index')
    context = {'todos': todos, 'form': form}
    return render(request, 'index.html', context)


def complete(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('my_app:index')


def delete(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('my_app:index')
