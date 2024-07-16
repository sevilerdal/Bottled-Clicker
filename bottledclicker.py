from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.bottledapp.com/auth/login")

email = "yourmail@mail.co" # Change this with your email address
passwd = "yourpassword" # Change this with your password
chatusername = "targetUsername" # Change this with the username of your friend


driver.find_element(by="xpath",value="//input[@type='email']").send_keys(email)
driver.find_element(by="xpath",value="//input[@type='password']").send_keys(passwd)
driver.find_element(by="xpath",value="//button[@type='submit']").click()

time.sleep(5)
driver.get("https://www.bottledapp.com/app/chat")

time.sleep(5)
driver.find_element(by="xpath", value=f"//img[@alt='{chatusername}']").click()
time.sleep(5)

driver.find_element(by="xpath", value="//body").send_keys(Keys.CONTROL + Keys.HOME)



try:
    while True:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Load older messages')]"))).click()
except WebDriverException as e:
    time.sleep(600)




driver.close()