from django.test import TestCase
from django.urls import reverse
from Todo_list.models import Tag

class TagTests(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, "Test Tag")

    def test_tag_update(self):
        url = reverse("todo:update_tag", args=[self.tag.id])
        response = self.client.post(url, {"name": "Updated Tag"})
        self.assertEqual(response.status_code, 302)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "Updated Tag")

    def test_tag_delete(self):
        url = reverse("todo:delete_tag", args=[self.tag.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(id=self.tag.id).exists())
