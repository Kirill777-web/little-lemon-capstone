from django.test import TestCase
from .models import Menu
# Create your tests here.


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Lemon Cake", price=10, inventory=3)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "Lemon Cake - 10")
