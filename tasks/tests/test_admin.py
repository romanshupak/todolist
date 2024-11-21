from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasks.models import Task, Tag


class AdminTest(TestCase):
    def setUp(self) -> None:
        """Set up test data and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="adminpassword"
        )
        self.client.force_login(self.admin_user)

        # Create a Task and Tag for testing
        self.tag = Tag.objects.create(name="Urgent")
        self.task = Task.objects.create(content="Test Task", is_done=False)

    def test_task_listed_in_admin(self):
        """Test that the Task model is listed in the admin panel."""
        url = reverse("admin:tasks_task_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.task.content)

    def test_tag_listed_in_admin(self):
        """Test that the Tag model is listed in the admin panel."""
        url = reverse("admin:tasks_tag_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.tag.name)

    def test_task_detail_view_in_admin(self):
        """Test the Task detail view in the admin panel."""
        url = reverse("admin:tasks_task_change", args=[self.task.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.task.content)

    def test_tag_detail_view_in_admin(self):
        """Test the Tag detail view in the admin panel."""
        url = reverse("admin:tasks_tag_change", args=[self.tag.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.tag.name)
