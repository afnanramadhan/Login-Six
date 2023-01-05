from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://akademik.itb.ac.id/home')
driver.maximize_window()
time.sleep(2)

login_btn = driver.find_element(By.ID, 'login')
login_btn.click()
time.sleep(2)

login_ina_btn = driver.find_element(By.LINK_TEXT, 'Login dengan INA')
login_ina_btn.click()
time.sleep(2)

