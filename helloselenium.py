import time
from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

done = "FAIL"
baseurl = "http://www.google.com"

mydriver = webdriver.Chrome()
mydriver.get(baseurl)
mydriver.maximize_window()

mydriver.find_element_by_id("lst-ib").send_keys("seleniumhq")
mydriver.find_element_by_class_name("lsb").click()

done = "Success"

if (done == "Success"):
    #Make the pyhton to wait for 5 seconds
   	time.sleep(5)	
	
	#Find the first link after getting the searched for Seleniumhq and click on the link. 
	mydriver.execute_script("return document.getElementsByClassName('rc')[0].getElementsByTagName('a')[0].click();")
	
	e = mydriver.execute_script("return document.getElementsByTagName('a')[0].getAttribute('title')")
	print e

	#Verify the link opened is for Selenium
	if "Selenium" in e:
		print "SUCESSFUL OPENED the correct link"
	
	#Verify the homepage is opened
	if(mydriver.find_element_by_class_name("homepage")):
		print "Selenium HOME WEB_PAGE is OPENED"
	else:
		print "FAILED TO OPEN THE WEB PAGE"
else:
	print done