from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
from loginsix import login

driver = webdriver.Chrome()
login(driver)

#masuk menu frs
driver.find_element(By.LINK_TEXT, 'Rencana Studi & Perwalian').click()

fakul = driver.find_element(By.NAME, 'fakultas')
fakul.click()

pilihFakul = driver.find_elements(By.TAG_NAME, 'option')
for i in pilihFakul:
    if i.text == 'STEI':
        i.click()
        break

prodi = driver.find_element(By.NAME, 'prodi')
prodi.click()

pilihJenjang = driver.find_element(By.XPATH, '//*[@id="prodi"]/optgroup[1]')
pilihProdi = pilihJenjang.find_elements(By.TAG_NAME, 'option')
for i in pilihProdi:
    if '135' in i.text:
        i.click()
        break

# refreshh = driver.find_element(By.ID, 'refresh')
# refreshh.click()

matkul = driver.find_element(By.PARTIAL_LINK_TEXT, 'Dasar Pemrograman')
matkul.click()

pilihanMatkul = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/form/div')

cariKelas = pilihanMatkul.find_elements(By.TAG_NAME, 'div')
for i in cariKelas:
    if '08' in i.text:
        print(i.text)
        kelas = i.find_element(By.PARTIAL_LINK_TEXT, 'Silabus')
        break

kelas.click()

balik = driver.find_element(By.PARTIAL_LINK_TEXT, 'Menu').click()
rencanaStudi = driver.find_element(By.PARTIAL_LINK_TEXT, 'Rencana Studi').click()

panelKanan = driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/form[1]/div')
print(panelKanan.text)

# kirim = panelKanan.find_element(By.PARTIAL_LINK_TEXT, 'Kirim')
# print(kirim.text)



while keyboard.is_pressed('Esc') == False:
    continue