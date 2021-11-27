from django.test import TestCase
from tasks.models import Username, Task, TaskForm, UsernameForm


class TestModels(TestCase):
    def setUp(self):
        self.project1 = Username.objects.create(
            username='adanger'
        ) 
        self.project2 = Username.objects.create(
            username='bwarning'
        ) 
        self.project3 = Username.objects.create(
            username='csuccess'
        ) 
        self.category1 = Task.objects.create(
            username=self.project1,
            title='Priority High'
        )
        self.category2 = Task.objects.create(
            username=self.project2,
            title='Priority Medium'
        )
        self.category3 = Task.objects.create(
            username=self.project3,
            title='Priority Low'
        )
    def test_priorities_high(self):
        self.assertEquals(self.project1.username, 'adanger')

    def test_priorities_medium(self):
        self.assertEquals(self.project2.username, 'bwarning')
        
    def test_project_low(self):
        self.assertEquals(self.project3.username, 'csuccess')