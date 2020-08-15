from django.shortcuts import render
import logging

from .models import Todolist

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):

    todo_items = Todolist.objects.order_by('id')

    context = {
        'todo_items': todo_items
    }
    logger.error(todo_items)
    return render(request, "todolist/index.html", context)


