
class LoginPage():
	# Locators for web elements
	textbox_username_id = 'txtUsername'
	textbox_password_id = 'txtPassword'
	button_login_id = 'btnLogin'
	link_user_linktext = 'Welcome'
	link_logout_linktext = 'Logout'

	def __init__(self, driver):
		self.driver = driver

	def setUserName(self, username):
		self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

	def setPassword(self, password):
		self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

	def clickLogin(self):
		self.driver.find_element_by_id(self.button_login_id).click()

	def clickLogout(self):
		self.driver.find_element_by_partial_link_text(self.link_user_linktext).click()
		self.driver.implicitly_wait(5)
		self.driver.find_element_by_link_text(self.link_logout_linktext).click()