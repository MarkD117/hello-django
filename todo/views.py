from django.shortcuts import render, redirect
from .models import Item

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "todo/todo_list.html", context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')  # name attribute value in form
        done = 'done' in request.POST  # checking if done checkbox is selected
        # Creating a new item by directing to the Item model and setting the
        # variables above to the values in the item model
        Item.objects.create(name=name, done=done)

        # returning user to get_todo_list view above
        return redirect('get_todo_list')
    return render(request, "todo/add_item.html")
