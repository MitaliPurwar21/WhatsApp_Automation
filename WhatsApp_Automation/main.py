# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path=r"D:\Projects\Python\edgedriver_win64\msedgedriver.exe")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # control the contact search textbox
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)

    # Replace 'Friend's Name' with the name of your friend
    # or the name of a group
    target = '"Mitali"'

    # Replace the below string with your own message
    string = "Message sent using Python!!!"

    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()
    inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
    search = driver.find_elements_by_class_name(r"p3_M1")
    # input_box = wait.until(EC.presence_of_element_located(( By.XPATH, inp_xpath)))
    for i in range(3):
        search[0].send_keys(string + Keys.ENTER)
        time.sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
