import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


print("Wait bruhh\nVS :)")

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)


driver.get('https://monkeytype.com/')

driver.maximize_window()
try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.active.acceptAll'))
    )
    button.click()
except TimeoutException:
    print("Timed out waiting for the button to be clickable")

start_time = time.time()
duration = 30

while time.time() - start_time < duration:
    try:
        word_active = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.word.active'))
        )
        py.typewrite(word_active.text)
        py.press('space')

    except TimeoutException:
        print('No words detected.')
        break


time.sleep(30)
driver.quit()
