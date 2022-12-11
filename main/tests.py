from django.test import TestCase

# Create your tests here.
class URLTest(TestCase):
    def test_main_page_url(self):
        response = self.client.get('/main/')
        self.assertTrue(response.status_code == 200)
    def test_fake_url(self):
        response = self.client.get('/fake/')
        self.assertFalse(response.status_code == 200)