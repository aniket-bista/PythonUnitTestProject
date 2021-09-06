from selenium import webdriver
import unittest
import HtmlTestRunner

class OrangeHRMLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:\\WebDrivers\\chromedriver_win32\\chromedriver.exe')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('OrangeHRM Login Test Completed ... ')

    def test_homePageTitle(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.assertEqual('OrangeHRM123', self.driver.title, 'Webpage titles are not same ')

    def test_login(self):
        self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        self.driver.find_element_by_id('btnLogin').click()
        self.assertEqual('OrangeHRM', self.driver.title, 'Webpage titles are not same ')

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\aniket bista\\PythonUnitTestProject\\Report'))
