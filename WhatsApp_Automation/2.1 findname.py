"""
Whatsapp automation using Python

Source code to demonstrate the find_element_by_name().
"""

#import the webdriver from selenium package
from selenium import webdriver

#import the keys class from selenium package
from selenium.webdriver.common.keys import Keys


#initialize the web driver variable
driver = webdriver.Chrome(executable_path = r"") #give the path of the web driver in the string

#browse to a particular location
driver.get(r"test.html") #give the path of the test.html

#create a variable to control the name textbox present in the test.html
txt1=driver.find_element_by_name("name")

#type "abcd" in the textbox
txt1.send_keys("abcd")

#create a variable to control the two textboxes with same name
txt2=driver.find_elements_by_name("phno")

#type 100 in first textbox
txt2[0].send_keys("100")

#type 200 in second textbox
txt2[1].send_keys("100")