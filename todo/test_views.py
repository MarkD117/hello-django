from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # handling CRUD functionality by creating an item
        item = Item.objects.create(name='Test Todo Item')
        # we can access the created items id through an f string
        # using a get request to edit the item
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # posting a name to the /add url to create an item
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # if item added successfully, it should redirect to home
        self.assertRedirects(response, '/')

    def test_can_delete_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        # using get request to delete the item
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # checking if item is deleted by filtering by id
        existing_items = Item.objects.filter(id=item.id)
        # filter result should be 0 as no item with that id exists
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item_page(self):
        # create item with done status of True
        item = Item.objects.create(name='Test Todo Item', done=True)
        # call toggle request on created item
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        # get the id of the created item
        updated_item = Item.objects.get(id=item.id)
        # check if done status changed to False
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        # posting an edit to item changing name
        response = self.client.post(
            f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
