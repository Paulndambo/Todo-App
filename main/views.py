from django.shortcuts import render
from django.utils import timezone
from . models import Todo
from django.http import HttpResponseRedirect

def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'index.html', {
    "todo_items": todo_items
    })


def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    title = request.POST["title"]
    created_obj = Todo.objects.create(
        added_date=current_date, 
        text=content,
        title=title
    )
    print(created_obj)
    print(created_obj.id)
    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
