from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import time
from loginsix import login

f = open('tandaiHadir.txt', 'r')
tglMK = f.readlines()
tglMK = list(map(lambda x:x.strip(),tglMK))
tanggal = str(time.localtime()[2])


driver = webdriver.Chrome()

login(driver)

#open menu class
kelas = driver.find_element(By.LINK_TEXT, 'Kelas')
kelas.click()


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
        if tanggal in tgll.text:
            try:
                matkul = j.find_element(By.PARTIAL_LINK_TEXT, tglMK[1]).click()
                break
            except:
                print("TIDAK ADA MATKUL", tglMK[1], "HARI INI")


action = ActionChains(driver)
# klik tandai hadir
try:
    time.sleep(2)
    tandaiHadir = driver.find_element(By.XPATH, '//*[@id="form_hadir"]')
    print(tandaiHadir.is_enabled())
    print(tandaiHadir.is_selected())
    print(tandaiHadir.text)
    # form = tandaiHadir.find_element(By.ID, 'form_hadir')
    print('----------------------')
    # print(form.is_enabled())
    # print(form.is_selected())
    # print(form.text)
    # pencet = tandaiHadir.find_element(By.TAG_NAME, 'form')
    # tandaiHadir.click()
    time.sleep(2)
    action.move_to_element(tandaiHadir).click().perform()
    print("berhasil")
    yutup = driver.execute_script('''window.open("https://www.youtube.com/watch?v=13ARO0HDZsQ","_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    try:
        play = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[5]/button')
        action.move_to_element(play).click().perform()
    except:
        play = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[1]/video')
        action.move_to_element(play).click().perform()
        
    
    # ##skip iklan
    time.sleep(8)
    try:
        skip = driver.find_element(By.CLASS_NAME, 'ytp-ad-player-overlay-skip-or-preview')
        print(skip.is_enabled())
        print(skip.is_selected())
        print(skip.text)
        print("----------------------")
        butonSkip = skip.find_element(By.TAG_NAME, 'button')
        if skip.text == 'Skip Ads':
            action.move_to_element(butonSkip).click().perform()
    except:
        print('GAK ADA IKLAN YANG BISA DI SKIP')
    
    print("berhasil")
except:
    print('Tidak ada pertemuan')
    yutup = driver.execute_script('''window.open("https://www.youtube.com/watch?v=V37TaRdVUQY","_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    try:
        play = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[5]/button')
        action.move_to_element(play).click().perform()
    except:
        play = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[1]/video')
        action.move_to_element(play).click().perform()
    
    ##skip iklan
    time.sleep(8)
    try:
        skip = driver.find_element(By.CLASS_NAME, 'ytp-ad-player-overlay-skip-or-preview')
        print(skip.is_enabled())
        print(skip.is_selected())
        print(skip.text)
        print("----------------------")
        butonSkip = skip.find_element(By.TAG_NAME, 'button')
        if skip.text == 'Skip Ads':
            action.move_to_element(butonSkip).click().perform()
    except:
        print('GAK ADA IKLAN YANG BISA DI SKIP')




while keyboard.is_pressed('Esc') == False:
    continue


