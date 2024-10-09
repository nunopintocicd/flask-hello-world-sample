import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_cpu_load(self):
        response = self.client.get('/cpu')
        self.assertEqual(response.status_code, 200)

    def test_memory_load(self):
        response = self.client.get('/memory')
        self.assertEqual(response.status_code, 200)

    def test_io_load(self):
        response = self.client.get('/io')
        self.assertEqual(response.status_code, 200)

    def test_network_load(self):
        response = self.client.get('/network')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()