from selenium import webdriver
import unittest
import HtmlTestRunner

import sys
sys.path.append('..\\POMBasedProject')
from pageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
	baseURL = 'https://opensource-demo.orangehrmlive.com/'
	username = 'Admin'
	password = 'admin123'
	driver = webdriver.Chrome(executable_path='C:\\WebDrivers\\chromedriver_win32\\chromedriver.exe')

	@classmethod
	def setUpClass(cls):
		cls.driver.get(cls.baseURL)
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(5)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		print('OrangeHRM Login Test Completed ... ')

	def test_login(self):
		lp = LoginPage(self.driver)
		lp.setUserName(self.username)
		lp.setPassword(self.password)
		lp.clickLogin()
		self.driver.implicitly_wait(5)
		self.assertEqual('OrangeHRM', self.driver.title, 'Webpage titles are not same')

	def test_logout(self):
		lp = LoginPage(self.driver)
		lp.clickLogout()
		self.driver.implicitly_wait(5)
		self.assertEqual('OrangeHRM', self.driver.title, 'Webpage titles are not same')


if __name__=="__main__":
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=
		'..\\Report'))


