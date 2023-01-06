from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://akademik.itb.ac.id/home')
driver.maximize_window()
# time.sleep(2)

login_btn = driver.find_element(By.ID, 'login')
login_btn.click()
# time.sleep(2)

login_ina_btn = driver.find_element(By.LINK_TEXT, 'Login dengan INA')
login_ina_btn.click()
# time.sleep(2)

with open('Login-Six/pass.txt', 'r') as x:
    password = x.read()
with open('Login-Six/nim.txt', 'r') as x:
    nim = x.read()

uname = driver.find_element(By.NAME, 'username')
uname.send_keys(nim)
pwd = driver.find_element(By.NAME, 'password')
pwd.send_keys(password)
# time.sleep(2)
submit = driver.find_element(By.NAME, 'submit')
submit.click()
# time.sleep(2)

kelas = driver.find_element(By.LINK_TEXT, 'Kelas')
kelas.click()

matdis1 = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[1]/td[1]/div[2]/div[1]/a")
matdis1.click()

tandaiHadir = driver.find_element(By.LINK_TEXT, 'Tandai Hadir')
tandaiHadir.click()

time.sleep(100)


