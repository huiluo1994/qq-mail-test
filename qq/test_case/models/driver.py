from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器驱动
def browser():
	driver = webdriver.Firefox()
	'''
	host = "127.0.0.1:4444" #运行主机：端口号（本机默认：127.0.0.1:4444）
	dc = {"browser": "Firefox"} #指定浏览器
	driver = Remote(command_executor = "http://" + host + "/wd/hub", desired_capabilities = dc)
	'''
	return driver

if __name__ == "__main__":
	dr = browser()
	dr.get("https://www.baidu.com")
	dr.quit()


