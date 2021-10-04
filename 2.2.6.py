from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)
    input3 = browser.find_element_by_id("robotCheckbox")
    input3.click()
    input4 = browser.find_element_by_css_selector("[value='robots']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input4)
    input4.click()
   

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    

finally:
    
    time.sleep(10)
    browser.quit()