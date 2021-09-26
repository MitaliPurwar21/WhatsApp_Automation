"""
Whatsapp automation using Python

Source code to demonstrate the find_element_by_link_text().
"""

#import the webdriver from selenium package
from selenium import webdriver

#import the keys class from selenium package
from selenium.webdriver.common.keys import Keys


#initialize the web driver variable
driver = webdriver.Chrome(executable_path = r"") #give the path of the web driver in the string

#browse to a particular location
driver.get(r"test.html") #give the path of the test.html

#create a variable to control the link button present in the test.html
link=driver.find_element_by_link_text("View help")

#click the button
link.click()
