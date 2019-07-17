from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.by import By 
from .base import Page
from time import sleep
from selenium import webdriver

class Login(Page):
	'''
	Login interface
	'''

	def login(self):
		xp = self.driver.find_element_by_xpath('//*[@id="login_frame"]')
		self.driver.switch_to.frame(xp)
		self.login_username_loc = (By.XPATH, "//*[@id='u']")
		self.login_password_loc = (By.XPATH, "//*[@id='p']")
		self.login_button_loc = (By.XPATH, "//*[@id='login_button']")

	def login_username(self, username):
		self.find_element(*self.login_username_loc).send_keys(username)

	def login_password(self, password):
		self.find_element(*self.login_password_loc).send_keys(password)

	def login_button(self):
		self.find_element(*self.login_button_loc).click()

	#定义统一登录入口
	def user_login(self, username = "username", password = "password"):
		self.open("/")
		self.login()
		self.login_username(username)
		self.login_password(password)
		self.login_button()
		#self.driver.switch_to.default_content()

	#user_error_hint_loc = (By.XPATH, "//*[@id='error_tips']")
	#user_login_success_loc = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div[1]/a[3]")

	#登录错误
	def user_error_hint(self):
		self.user_error_hint_loc = (By.XPATH, "//*[@id='error_tips']")
		return self.find_element(*self.user_error_hint_loc).text

	#登录成功
	def user_login_success(self):
		self.driver.switch_to.default_content()
		self.user_login_success_loc = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div[1]/a[3]")
		return self.find_element(*self.user_login_success_loc).text

if __name__ == "__main__":
	driver = webdriver.Firefox()
	page = Login(driver)
	#page.open("/")
	#page.login()
	#page.user_login(username = "")
	#print(page.user_error_hint())
	page.user_login("qq_mail", "qq_password")
	sleep(5)
	print(page.user_login_success())
	driver.quit()

	
	

	