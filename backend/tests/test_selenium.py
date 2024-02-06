import unittest
from selenium import webdriver

class TestApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:5000')

    def test_home_page(self):
        assert 'Hello, World!' in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()