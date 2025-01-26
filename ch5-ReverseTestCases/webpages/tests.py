from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_exists(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_template_content(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Welcome to Django!!!</h1>')
        

class HomePageAbsoluteUrlTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_exists(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
    
    def test_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Welcome to Django!!!</h1>')
    
class AboutPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_available(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')
        
    def test_template_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<h1>About Us!</h1>')