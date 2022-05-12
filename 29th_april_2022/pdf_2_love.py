from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\ash\Desktop\python_practise\selenium\29th_april_2022\chromedriver_win32\chromedriver.exe")
driver.get('https://www.w3schools.com/html/html_exercises.asp')
# driver.manage().timeouts().pageLoadTimeout(100, SECONDS);

# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div/a[1]/div[2]"))).click()
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div/div[1]/div/div/span"))).click()
# element_1 = driver.find_element_by_xpath(( By.XPATH, '//*[@id="pickfiles"]'))
# element_1.SendKeys("C://Users/ash/Downloads/3._How_to_Use_Container_Widgets.mp4");

driver.implicitly_wait(1.5)
driver.maximize_window()

# element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="pickfiles"]'))  # Example xpath

# # WebDriverWait(driver, 10).until(element_present).click() # This opens the windows file selector
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pickfiles"]'))).click()
# pyautogui.click(100, 200)
# time.sleep(3)
# pyautogui.write('C:\\Users\\ash\\Pictures\\7.jpg')

# print("Done")
# pyautogui.press('enter')
# time.sleep(5)
# # driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# #to identify element
# # s = driver.find_element(( By.XPATH, r"//input[@type='file']"))
# #file path specified with send_keys
# # s.send_keys("C:\\Users\\ash\\Pictures\\7.jpg")
# # element.SendKeys("C:\\Some_Folder\\MyFile.txt");
action = webdriver.ActionChains(driver)
# # element = driver.find_element_by_id('your-id') # or your another selector here
# # action.move_to_element(element)
# # action.perform()

# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="processTask"]'))).click()
# time.sleep(5)

# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pickfiles"]'))).click()
# action = webdriver.ActionChains(driver)
# element = driver.find_element_by_xpath('//*[@id="menuBig"]/ul/li[4]/span')# or your another selector here
# action.move_to_element(element)
# action.perform()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# action.move_by_offset(100, 200).perform()






liElement = driver.find_element_by_xpath('//*[@id="leftmenuinnerinner"]')
h2_element = liElement.find_elements_by_xpath('//*[@id="leftmenuinnerinner"]/h2[1]')


# liElement.click()



actions = ActionChains(driver)
actions.move_to_element(liElement).perform()




# driver.execute_script("arguments.scrollBy(0,arguments[0].scrollHeight)", liElement)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("arguments[0].scrollIntoView();", liElement)
# liElement.location_once_scrolled_into_view
# driver.execute_script("arguments[0].scrollIntoView(true);", liElement);
# print(liElement.text)
# desired_y = (liElement.size['height'] * 2) + liElement.location['y']
# current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
# scroll_y_by = desired_y - current_y
# driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
# target = driver.find_element_by_link_text('HTML Tutorial')
# actions.move_to_element(target)
# div_locator = "xpath_locator"
# ScrollNumber = 50
# for i in range(1,ScrollNumber):
#     driver.execute_script("window.scrollTo(1,50000)")
#     time.sleep(5)
    
# div_el = driver.find_element_by_xpath(div_locator)
for i in range(20):
  driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", liElement)
  time.sleep(random.randint(200,500)/1000)
  actions.perform()
  print(driver.page_source)

# action.scroll(400, 25).perform()
# driver.execute_script("window.scrollTo(0, 400);") 


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument("--auto-open-devtools-for-tabs")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options, executable_path=r'C:\Utility\BrowserDrivers\chromedriver.exe')
# driver.get("https://selenium.dev/documentation/en/")
print(driver.page_source)
time.sleep(8)
