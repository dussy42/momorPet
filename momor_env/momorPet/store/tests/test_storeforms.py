from django.test import SimpleTestCase
from store.forms import OrderForm, ProductForm


class FormTest(SimpleTestCase):

    def test_order_form_valid_data(self):

        form_data = {
            'title': 'Exeleron',
            'price': 2000,

        }

        form = OrderForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_order_form_invalid_data(self):

        form_data = {

        }

        form = OrderForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_order_form_missing_required_field(self):

        form_data = {
            'price': 2,

        }

        form = OrderForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertTrue('title' in form.errors)
