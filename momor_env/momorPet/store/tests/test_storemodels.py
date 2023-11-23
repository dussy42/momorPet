from django.test import TestCase, Client
from django.urls import reverse
from store.models import OrderItem, Order, Product, Category
from django.core.exceptions import ValidationError


class Test_store_models(TestCase):
    def test_slug_is_generated_when_title_is_set(self):
        category = Category(title='Cars')
        category.save()
        self.assertEqual(category.slug, 'cars')

    def test_slug_is_unique(self):
        Category.objects.create(title='Cars', slug='cars')
        category2 = Category(title='Cars')
        category2.save()
        self.assertNotEqual(category2.slug, 'cars')

    def test_get_absolute_url(self):
        category = Category(title='Cars', slug='cars')
        self.assertEqual(category.get_absolute_url(), reverse(
            'category_detail', args=[category.slug]))

    def test_product_title_is_required(self):
        product = Product()
        product.save()
        self.assertRaisesMessage(
            ValidationError, 'This field can not be empty', product.title)

    def test_product_slug_is_generated_when_title_is_set(self):
        product = Product(title='Exeleron')
        product.save()
        self.assertEqual(product.slug, 'exeleron')

    def test_product_slug_is_unique(self):
        Product.objects.create(title='Exeleron', slug='exeleron')
        product2 = Product(title='Exeleron')
        product2.save()
        self.assertNotEqual(product2.slug, 'exeleron')

    def test_get_absolute_url(self):
        product = Product(title='Exeleron', slug='exeleron')
        self.assertEqual(product.get_absolute_url(), reverse(
            'product_detail', args=[product.slug]))

    def test_order_creation(self):

        order = Order.objects.create(
            first_name='Momoh',
            last_name='sam',
            address='ireland',
            zipcode=5050,
            city='Dublin'
        )

        saved_order = Order.objects.get(first_name='Momoh')

        self.assertEqual(saved_order.first_name, 'Momoh')
        self.assertEqual(saved_order.last_name, 'sam')
        self.assertEqual(saved_order.address, 'ireland')
        self.assertEqual(saved_order.zipcode, '5050')
        self.assertEqual(saved_order.city, 'Dublin')

    def setUp(self):

        self.product = Product.objects.create(
            title='Exeleron',
            price=50.00,

        )

    def test_order_item_creation(self):

        order_item = OrderItem.objects.create(
            product=self.product,
            quantity=2,

        )

        saved_order_item = OrderItem.objects.get(pk=order_item.pk)

        self.assertEqual(saved_order_item.product, self.product)
        self.assertEqual(saved_order_item.quantity, 2)
