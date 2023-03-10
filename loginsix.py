from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard


#read nim and password from file
f = open('nimPass.txt', 'r')
nimPass = f.readlines()
nimPass = list(map(lambda x:x.strip(),nimPass)) #delete \n


def login(driver):
    #open browser
    
    driver.get('https://akademik.itb.ac.id/home')
    driver.maximize_window()

    #click login button
    login_btn = driver.find_element(By.ID, 'login')
    login_btn.click()

    #click login with INA button
    login_ina_btn = driver.find_element(By.LINK_TEXT, 'Login dengan INA')
    login_ina_btn.click()

    #input nim and password
    uname = driver.find_element(By.NAME, 'username')
    uname.send_keys(nimPass[0])
    pwd = driver.find_element(By.NAME, 'password')
    pwd.send_keys(nimPass[1])
    submit = driver.find_element(By.NAME, 'submit')
    submit.click()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login(driver)
    
    while keyboard.is_pressed('q') == False:
        continue