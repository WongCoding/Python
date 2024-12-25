from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url1 = 'https://cn.bing.com/'
driver = webdriver.Chrome()

driver.get(url1)
sleep(1)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys("oppo解散芯片研发团队")
driver.find_element_by_xpath('//*[@id="search_icon"]').click()

sleep(3)
driver.find_element_by_xpath('//*[@id="sb_form_q"]').clear()
driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys("公积金贷款条件", Keys.ENTER)
sleep(3)
driver.back()
sleep(7)

driver.close()

print("hello world")