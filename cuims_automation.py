from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome('C:\\Users\\Javed\\webdriver\\chromedriver.exe')
driver.get('https://uims.cuchd.in/uims/')


driver.find_element_by_id("txtUserId").send_keys("18bcs6705")
driver.find_element_by_id("btnNext").click()
driver.find_element_by_id("txtLoginPassword").send_keys("Javed@@1234")
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_class_name("toggle-btn").click()
#element=driver.find_element_by_xpath("div[li/@class='a-uims-nav']")
#all_option=driver.find_element_by_class_name("a-uims-nav")
element=Select(driver.find_element_by_id("uims_sidebar"))


print(element.select_by_indexy(4))



time.sleep(5)