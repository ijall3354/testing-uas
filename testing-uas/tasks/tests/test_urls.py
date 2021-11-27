from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tasks.views import complete, delete, tasks


class TestUrls(SimpleTestCase):

    def test_delete_task_url_is_resolved(self):
        url = reverse('delete_task', args=[1])
        self.assertEquals(resolve(url).func, delete)

    def test_completed_task_url_is_resolved(self):
        url = reverse('completed_task', args=[1])
        self.assertEquals(resolve(url).func, complete)

    def test_tasks_url_is_resolved(self):
        url = reverse('tasks')
        self.assertEquals(resolve(url).func, tasks)