from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time


#read nim and password from file
f = open('nimPass.txt', 'r')
nimPass = f.readlines()
nimPass = list(map(lambda x:x.strip(),nimPass)) #delete \n


def login(driver, pilih=1):
    #open browser
    
    driver.get('https://akademik.itb.ac.id/home')
    driver.maximize_window()

    #click login button
    login_btn = driver.find_element(By.ID, 'login')
    login_btn.click()

    #click login with INA button
    login_ina_btn = driver.find_element(By.LINK_TEXT, 'Login dengan ITB Account')
    login_ina_btn.click()
    

    #input email
    time.sleep(2)
    email = driver.find_element(By.XPATH, '//*[@id="i0116"]')
    email.send_keys(nimPass[0])
    driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    
    #input password
    time.sleep(2)
    pwd = driver.find_element(By.NAME, 'passwd')
    pwd.send_keys(nimPass[1])
    driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    
    #two factor authentication
    time.sleep(2)
    driver.find_element(By.XPATH, f'//*[@id="idDiv_SAOTCS_Proofs"]/div[{pilih}]').click()

    print("Klik esc jika sudah masuk six")

    while True:
        if keyboard.is_pressed('esc') == True:
            print('esc pressed')
            break
    print('done')


if __name__ == '__main__':
    x = int(input("choose verification methode:\n1 for verification code\n2 for approve request\n3 for text\n4 for call\n>"))
    driver = webdriver.Chrome()
    login(driver,x)
    
    while keyboard.is_pressed('q') == False:
        continue