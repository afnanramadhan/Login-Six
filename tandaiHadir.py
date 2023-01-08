from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import keyboard

f = open('tandaiHadir.txt', 'r')
tglMK = f.readlines()
tglMK = list(map(lambda x:x.strip(),tglMK))


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

# with open('Login-Six/pass.txt', 'r') as x:
#     password = x.read()
# with open('Login-Six/nim.txt', 'r') as x:
#     nim = x.read()

uname = driver.find_element(By.NAME, 'username')
uname.send_keys('13521011')
pwd = driver.find_element(By.NAME, 'password')
pwd.send_keys('mhsITB109193')
# time.sleep(2)
submit = driver.find_element(By.NAME, 'submit')
submit.click()
# time.sleep(2)

kelas = driver.find_element(By.LINK_TEXT, 'Kelas')
kelas.click()

sem = driver.find_element(By.PARTIAL_LINK_TEXT, 'Semester 2')
sem.click()

sem1 = driver.find_element(By.LINK_TEXT, 'Semester 1 - 2022/2023')
sem1.click()

des = driver.find_element(By.LINK_TEXT, 'Nov 2022')
des.click()


kalender = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody")
print(kalender.is_enabled())



row = kalender.find_elements(By.TAG_NAME, 'tr')

print(type(row))
for i in row:
    # print(i.text)
    if tglMK[0] in i.text:
        baris = i.find_elements(By.TAG_NAME, 'td')
        break

for i in baris:
    if tglMK[0] in i.text:
        tgl = i.find_elements(By.TAG_NAME, 'div')
        break

for i in tgl:
    if tglMK[1] in i.text:
        pencet = i.find_element(By.PARTIAL_LINK_TEXT, tglMK[1])
        break
pencet.click()

# tandaiHadir = driver.find_element(By.LINK_TEXT, 'Tandai Hadir')
# tandaiHadir.click()

print("selesai")
# pencet.click()
# pencet = driver.find_element(By.PARTIAL_LINK_TEXT, ya)
# action = ActionChains(driver)
# action.double_click(pencet).perform()

# matdis1 = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[1]/td[1]/div[2]/div[1]/a")
# matdis1.click()

# tandaiHadir = driver.find_element(By.LINK_TEXT, 'Tandai Hadir')
# tandaiHadir.click()

while keyboard.is_pressed('Esc') == False:
    continue


