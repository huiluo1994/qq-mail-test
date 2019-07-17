from time import sleep
import unittest, random, sys
from selenium import webdriver
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import Login 

class LoginTest(myunit.MyTest):
	'''login test'''

	# test login
	def user_login_verify(self, username="", password=""):
		Login(self.driver).user_login(username, password)

	def test_login1(self):
		'''empty username'''
		self.user_login_verify()
		po = Login(self.driver)
		self.assertEqual(po.user_error_hint(), "你还没有输入帐号！")
		function.insert_img(self.driver, "empty_username.png")

	def test_login2(self):
		'''wrong username'''
		self.user_login_verify(username = "1234")
		po = Login(self.driver)
		self.assertEqual(po.user_error_hint(), "请输入正确的帐号！")
		function.insert_img(self.driver, "wrong_username.png")

	def test_login3(self):
		'''empty password'''
		self.user_login_verify(username = "913026748")
		po = Login(self.driver)
		self.assertEqual(po.user_error_hint(), "你还没有输入密码！")
		function.insert_img(self.driver, "empty_password.png")

	def test_login4(self):
		'''wrong username or wrong password'''
		self.user_login_verify(username = "913026748", password = " 1233456")
		po = Login(self.driver)
		self.assertEqual(po.user_error_hint(), "你输入的帐号或密码不正确，请重新输入。")
		function.insert_img(self.driver, "wrong_username_or_password.png")

	def test_login5(self):
		'''login success'''
		self.user_login_verify(username = "913026748", password = "qq_password")
		po = Login(self.driver)
		sleep(5)
		self.assertEqual(po.user_login_success(), "退出")
		function.insert_img(self.driver, "success.png")

if __name__ == "__main__":
	
	unittest.main()