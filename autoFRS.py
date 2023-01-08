from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard

# f = open('nimPass.txt', 'r')
# nimPass = f.readlines()
# nimPass = list(map(lambda x:x.strip(),nimPass)) #delete \n


driver = webdriver.Chrome()
driver.get('https://akademik.itb.ac.id/app/R/mahasiswa:13521011+2022-2/registrasI/mk/2021010986/kelas?fakultas=STEI&prodi=135')
driver.maximize_window()


#click login with INA button
login_ina_btn = driver.find_element(By.LINK_TEXT, 'Login dengan INA')
login_ina_btn.click()

#input nim and password
uname = driver.find_element(By.NAME, 'username')
uname.send_keys('13521011')
pwd = driver.find_element(By.NAME, 'password')
pwd.send_keys('mhsITB109193')
submit = driver.find_element(By.NAME, 'submit')
submit.click()

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