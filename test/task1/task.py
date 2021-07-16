from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')

driver.get("https://khaadi.com/")
driver.find_element_by_xpath('//*[@id="countrydropdown"]/input').click()
print(driver.title)
driver.close()