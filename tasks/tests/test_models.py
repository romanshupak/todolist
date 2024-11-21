from django.test import TestCase
from tasks.models import Task, Tag


class ModelTests(TestCase):
    def test_tag_str(self):
        """Test the string representation of the Tag model."""
        tag = Tag.objects.create(name="Urgent")
        self.assertEqual(str(tag), tag.name)

    def test_task_str(self):
        """Test the string representation of the Task model."""
        task = Task.objects.create(content="This is a test task")
        self.assertEqual(str(task), task.content[:50])

    def test_task_default_is_done(self):
        """Test that the default value of 'is_done' is False."""
        task = Task.objects.create(content="Default status test")
        self.assertFalse(task.is_done)

    def test_task_tags_relationship(self):
        """Test the many-to-many relationship between Task and Tag."""
        tag1 = Tag.objects.create(name="Important")
        tag2 = Tag.objects.create(name="Work")
        task = Task.objects.create(content="Task with tags")
        task.tags.add(tag1, tag2)
        self.assertIn(tag1, task.tags.all())
        self.assertIn(tag2, task.tags.all())
        self.assertEqual(task.tags.count(), 2)
