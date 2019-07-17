from HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os

def new_report(testreport):
	lists = os.listdir(testreport)
	lists.sort(key = lambda fn: os.path.getmtime(testreport + '/' + fn))
	file_new = os.path.join(testreport, lists[-1])
	print(filr_new)
	return file_new

if __name__ == "__main__":
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = "./qq/report/" + now + "result.html"
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream = fp, title = "qq mail test report", description = "browser: firefox")
	discover = unittest.defaultTestLoader.discover("./qq/test_case", pattern = "*_sta.py", top_level_dir = None)
	runner.run(discover)
	fp.close()
