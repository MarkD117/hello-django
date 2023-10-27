from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # instantiating form without name value to simulate
        # a user that submits without a name
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        # When form is invalid, it sends back a dict of fields
        # on which there was errors with associated error messages.
        # assertIn() is used to check if a name key caused an error
        self.assertIn('name', form.errors.keys())
        # Checking that the name error message matches. zero index used
        # as the form will return list of errors on each field. This
        # verifies that the first item in that list is our string telling
        # us the field is required.
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_meta_class(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
