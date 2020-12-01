import unittest
import app
import xmlrunner

class TestExample(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()
    
    def test_example(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
