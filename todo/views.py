from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "todo/todo_list.html", context)


def add_item(request):
    if request.method == 'POST':
        # populating the form in Django with the request.POST data
        form = ItemForm(request.POST)
        # checking if the form data is valid
        if form.is_valid():
            # saves form data
            form.save()
            # returning user to get_todo_list view above
            return redirect('get_todo_list')
    # create an instance of the imported form in the add_item view.
    # Create a context which contains the empty form. And then return
    # the context to the template.
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, "todo/add_item.html", context)
