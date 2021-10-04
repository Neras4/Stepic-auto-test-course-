from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button")
    button.click()

    input1 = browser.switch_to.alert
    input1.accept()

    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()


    

    

finally:
    
    time.sleep(10)
    browser.quit()