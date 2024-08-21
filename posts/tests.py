from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class PostTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.post = Post.objects.create(text='this is test text')
    
  def test_model_content(self):
    self.assertEqual(self.post.text, 'this is test text')
    
  def test_url_exists_at_correct_location(self): # new
    response = self.client.get("/")
    self.assertEqual(response.status_code, 200)
    
  def test_url_available_by_name(self): # new
    response = self.client.get(reverse("home"))
    self.assertEqual(response.status_code, 200)
    
  def test_template_name_correct(self): # new
    response = self.client.get(reverse("home"))
    self.assertTemplateUsed(response, "home.html")
    
  def test_homepage(self): # new
    response = self.client.get(reverse("home"))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "home.html")
    self.assertContains(response, "This is a test!")