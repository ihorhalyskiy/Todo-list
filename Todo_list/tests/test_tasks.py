from django.test import TestCase
from django.urls import reverse
from Todo_list.models import Task, Tag
from django.utils import timezone

class TaskTests(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(content="Test Task", deadline=timezone.now())
        self.task.tags.add(self.tag)

    def test_task_creation(self):
        self.assertEqual(self.task.content, "Test Task")
        self.assertEqual(self.task.deadline.date(), timezone.now().date())

    def test_task_update(self):
        url = reverse("todo:update_task", args=[self.task.id])
        new_deadline = timezone.now().isoformat()
        response = self.client.post(url, {
            "content": "Updated Task",
            "deadline": new_deadline,
            "tags": [self.tag.id],
        })
        print(response.content)
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, "Updated Task")
        self.assertEqual(self.task.deadline.date(), timezone.now().date())

    def test_task_delete(self):
        url = reverse("todo:delete_task", args=[self.task.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
