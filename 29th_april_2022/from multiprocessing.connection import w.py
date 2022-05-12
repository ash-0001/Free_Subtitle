from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = webdriver.Chrome(r".\chromedriver_win32\chromedriver.exe")
driver.get('https://stackoverflow.com/questions')
# driver.manage().timeouts().pageLoadTimeout(100, SECONDS);

# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div/a[1]/div[2]"))).click()
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div/div[1]/div/div/span"))).click()
# element_1 = driver.find_element_by_xpath(( By.XPATH, '//*[@id="pickfiles"]'))
# element_1.SendKeys("C://Users/ash/Downloads/3._How_to_Use_Container_Widgets.mp4");

driver.implicitly_wait(1.5)
driver.maximize_window()
# element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="pickfiles"]'))  # Example xpath

# WebDriverWait(driver, 10).until(element_present).click() # This opens the windows file selector
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="left-sidebar"]/div[1]')))
# pyautogui.click(100, 200)
# wait_var = WebDriverWait(driver,10)

# headless=wait_var.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="left-sidebar"]/div[1]')))

# action = webdriver.ActionChains(driver)
# action.move_by_offset(10, 20).perform()
# action.double_click()
# driver.execute_script("window.scrollBy(0, 500)", "")
# time.sleep(3)
# pyautogui.write('C:\\Users\\ash\\Pictures\\7.jpg')

# print("Done")
# pyautogui.press('enter')
# time.sleep(5)
# driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
#to identify element
# s = driver.find_element(( By.XPATH, r"//input[@type='file']"))
#file path specified with send_keys
# s.send_keys("C:\\Users\\ash\\Pictures\\7.jpg")
# element.SendKeys("C:\\Some_Folder\\MyFile.txt");
# action = webdriver.ActionChains(driver)
# element = driver.find_element_by_id('your-id') # or your another selector here
# action.move_to_element(element)
# action.perform()

# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="processTask"]'))).click()
# # time.sleep(5)

# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pickfiles"]'))).click()
# action = webdriver.ActionChains(driver)
# element = driver.find_element_by_xpath('//*[@id="menuBig"]/ul/li[4]/span')# or your another selector here
# action.move_to_element(element)
# action.perform()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
