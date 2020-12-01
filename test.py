import unittest
import app

class TestExample(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()
    
    def test_example(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
