"""
Whatsapp automation using Python

Source code to demonstrate the find_element_by_id().
"""

#import the webdriver from selenium package
from selenium import webdriver

#initialize the web driver variable
driver = webdriver.Chrome(executable_path = r"") #give the path of the web driver in the string

#browse to a particular location
driver.get(r"test.html") #give the path of the test.html

#create a variable to control the form present in the test.html
form=driver.find_element_by_id("form1")