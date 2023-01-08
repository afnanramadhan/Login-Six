from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
from loginsix import login

f = open('tandaiHadir.txt', 'r')
tglMK = f.readlines()
tglMK = list(map(lambda x:x.strip(),tglMK))


driver = webdriver.Chrome()
login(driver)

#open menu class
kelas = driver.find_element(By.LINK_TEXT, 'Kelas')
kelas.click()

sem = driver.find_element(By.PARTIAL_LINK_TEXT, 'Semester 2')
sem.click()

sem1 = driver.find_element(By.LINK_TEXT, 'Semester 1 - 2022/2023')
sem1.click()

des = driver.find_element(By.LINK_TEXT, 'Nov 2022')
des.click()

# select calender
kalender = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody")
print(kalender.is_enabled())

# bagi kalender jadi baris
row = kalender.find_elements(By.TAG_NAME, 'tr')

for i in row:
    #bagi baris jadi kolo,
    col = i.find_elements(By.TAG_NAME, 'td')
    for j in col:
        #cari tanggal dari tiap kolom per baris
        tgll = j.find_element(By.TAG_NAME, 'div')
        if tglMK[0] in tgll.text:
            press = j.find_element(By.PARTIAL_LINK_TEXT, tglMK[1])
            break

press.click()

# klik tandai hadir
try:
    tandaiHadir = driver.find_element(By.LINK_TEXT, 'Tandai Hadir')
    tandaiHadir.click()
    # driver.get('https://www.youtube.com/watch?v=13ARO0HDZsQ')
    yutup = driver.execute_script('''window.open("https://www.youtube.com/watch?v=13ARO0HDZsQ","_blank");''')
except:
    print('Tidak ada pertemuan')
    # driver.get('https://www.youtube.com/watch?v=pSUydWEqKwE')
    yutup = driver.execute_script('''window.open("https://www.youtube.com/watch?v=V37TaRdVUQY","_blank");''')


while keyboard.is_pressed('Esc') == False:
    continue


