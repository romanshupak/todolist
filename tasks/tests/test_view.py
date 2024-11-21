from django.test import TestCase
from django.urls import reverse
from tasks.models import Tag, Task


class TagsListViewTests(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Tag1")
        self.tag2 = Tag.objects.create(name="Tag2")
        self.url = reverse("tasks:tags-list")

    def test_tags_list_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_tags_list_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "tasks/tags_list.html")

    def test_tags_list_view_contains_tags(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.tag1.name)
        self.assertContains(response, self.tag2.name)


class CreateTagViewTests(TestCase):
    def setUp(self):
        self.url = reverse("tasks:tags-create")
        self.valid_data = {"name": "New Tag"}

    def test_create_tag_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_tag_successful(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())


class UpdateTagViewTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Old Tag")
        self.url = reverse("tasks:tags-update", args=[self.tag.pk])
        self.valid_data = {"name": "Updated Tag"}

    def test_update_tag_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_tag_successful(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "Updated Tag")


class DeleteTagViewTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Tag to Delete")
        self.url = reverse("tasks:tags-delete", args=[self.tag.pk])

    def test_delete_tag_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_delete_tag_successful(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(pk=self.tag.pk).exists())


class ToggleTaskStatusViewTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(content="Test Task", is_done=False)
        self.url = reverse("tasks:toggle-status", args=[self.task.pk])

    def test_toggle_task_status_view(self):
        self.assertFalse(self.task.is_done)

        self.client.post(self.url)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)

        self.client.post(self.url)
        self.task.refresh_from_db()
        self.assertFalse(self.task.is_done)