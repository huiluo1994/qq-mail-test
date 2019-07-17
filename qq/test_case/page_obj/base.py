from selenium import webdriver

class Page():

	bbs_url = "https://mail.qq.com"

	def __init__(self, driver, base_url = bbs_url, parent = None):
		self.base_url = base_url
		self.driver = driver
		self.timeout = 30
		self.parent = parent

	def open(self, url):
		url = self.base_url + url
		self.driver.get(url)
		assert self.on_page(url), "Did not land on %s" %url

	def on_page(self, url):
		return self.driver.current_url == url

	def find_element(self, *loc):
		return self.driver.find_element(*loc)

	def find_elements(self, *loc):
		return self.driver.find_elements(*loc)

	def script(self, src):
		return self.driver.execute_script(src)

if __name__ == "__main__":
	driver = webdriver.Firefox()
	page = Page(driver)
	page.open("/")
	driver.quit()