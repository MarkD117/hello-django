from django.shortcuts import render, redirect, get_object_or_404
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


# item_id parameter points to the item od attached to the edit button
def edit_item(request, item_id):
    # we want to get an instance of the item model. With an ID
    # equal to the item ID that was passed into the view via the URL.
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        # give form specific item instance we want to update
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # pass instance item to form to pre-populate it with the current items
    # details. This fills the form with the information above from the database
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)
