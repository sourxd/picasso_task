from django.test import TestCase

class TestFiles(TestCase):

    def test_files(self):
        response = self.client.get('/files/')
        self.assertEqual(response.status_code, 200)

    def test_upload(self):
        response = self.client.get('/upload/')
        self.assertEqual(response.status_code, 405)