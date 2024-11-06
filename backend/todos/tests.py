from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="test todo", body="simple testcase")

    def test_title(self):
        todo = Todo.objects.get(id=1)
        todo_title = f"{todo.title}"
        self.assertEqual(todo_title, "test todo")

    def test_body(self):
        todo = Todo.objects.get(id=1)
        todo_body = f"{todo.body}"
        self.assertEqual(todo_body, "simple testcase")
