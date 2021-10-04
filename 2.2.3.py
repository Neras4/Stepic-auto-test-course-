from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_id("num1")
    input2 = browser.find_element_by_id("num2")
    x = int(input1.text) + int(input2.text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x))
  

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    

finally:
    
    time.sleep(10)
    browser.quit()