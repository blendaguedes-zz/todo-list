from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect


def home(request):
    todo_items = Todo.objects.all().filter(done=False).order_by("-added_date")
    done_items = Todo.objects.all().filter(done=True).order_by("-done_date")
    done_data_list = Todo.objects.all().filter(done=True).order_by("-done_date").values_list('done_date', flat=True)
    done_data_list_str = [d.strftime('%d/%m/%y %H:%M:%S') for d in done_data_list]
    done_items = zip(done_items, done_data_list_str)
    return render(request, 'app/index.html', {'todo_items': todo_items, 'done_items': done_items})


@csrf_exempt
def add_todo(request):
    date = timezone.now()
    content = request.POST.get('content')
    Todo.objects.create(added_date=date, text=content, done=False)
    return HttpResponseRedirect('/')


@csrf_exempt
def mark_done(request, todo_id):
    obj = Todo.objects.get(id=todo_id)
    obj.done_date = timezone.now()
    obj.done = True
    obj.save()
    return HttpResponseRedirect('/')


@csrf_exempt
def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

@csrf_exempt
def alter(request, todo_id, text):
    obj = Todo.objects.get(id=todo_id)
    obj.text = text
    obj.save()
    return HttpResponseRedirect('/')