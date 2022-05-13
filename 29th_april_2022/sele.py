from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
# C:\Users\ash\downloads\yt1s.com - C in 100 Seconds_1080p.mp4
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import random
from bs4 import BeautifulSoup
x = random.randint(1, 6)
driver = webdriver.Chrome(executable_path=r"C:\Users\ash\Desktop\python_practise\selenium\29th_april_2022\chromedriver_win32\chromedriver.exe")
driver.get('https://www.veed.io/')
# driver.manage().timeouts().pageLoadTimeout(100, SECONDS);

# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div/a[1]/div[2]"))).click()
# # WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div/div[1]/div/div/span"))).click()
# time.sleep(15)
# element_1 = driver.find_element_by_xpath(( By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/span[2]/span"))
# element_1.SendKeys("C://Users/ash/Downloads/3._How_to_Use_Container_Widgets.mp4");
time.sleep(x)


driver.implicitly_wait(1.5)
driver.maximize_window()
# element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="pickfiles"]'))  # Example xpath
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div/a[1]/div[2]"))).click()
time.sleep(x)
# WebDriverWait(driver, 10).until(element_present).click() # This opens the windows file selector
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pickfiles"]'))).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/span[2]/span"))).click()
pyautogui.click(100, 200)
time.sleep(3)
pyautogui.write('C:\\Users\\ash\\downloads\\yt1s.com - C in 100 Seconds_1080p.mp4')

print("Done")
pyautogui.press('enter')


# //*[@id="dropWrapper-upload"]/div/div/nav/nav/a[3]
# element.SendKeys("C:\\Some_Folder\\MyFile.txt");

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dropWrapper-upload"]/div/div/nav/nav/a[3]'))).click()
print(" DONE Baby Boson's ")
time.sleep(5)
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[2]/button'))).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[2]/div/button'))).click()

action = webdriver.ActionChains(driver)
time.sleep(50)
wait_var = WebDriverWait(driver,10)
liElement=driver.find_element_by_xpath('//*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div')
button_xpath  = '//*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div/div' 
# button = driver.find_element_by_xpath(button_xpath)
# driver.execute_script("arguments[0].click();", button)
# headless=wait_var.until(EC.element_to_be_clickable((By.XPATH, liElement)))
amp=ActionChains(driver)
# actions = ActionChains(driver)
f = open("demofile3.txt", "w")
amp.move_to_element(liElement).perform()
for i in range(20):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", liElement)
    # time.sleep(2)
    amp.perform()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # time.sleep(1)
    # print("And Purified text is")
    tin = soup.findAll('textarea')
    # sup = BeautifulSoup(soup, '')
    time.sleep(1)
    mydivs = soup.findAll(
        "textarea", {"class": "TextEditorStyled__TextArea-sc-nw7y0k-1 iBnmpX"})
    # tex = mydivs.getText()TextEditorStyled__TextArea-sc-nw7y0k-1 iBnmpX
    kost = []
    for things in kost:
        soup = BeautifulSoup(str(mydivs), 'html.parser')

    soup = BeautifulSoup(str(mydivs), 'html.parser')
    find_span = soup.find_all("textarea")
    # print(type(find_span))
    soup = BeautifulSoup(str(find_span), 'html.parser')
    tim = soup.get_text()

    m = tim.replace("[", "")
    n = m.replace("]", "")
    L = n.split(',')
  
  
  
    f.write(tim)
  # print(driver.page_source)

# action.scroll(400, 25).perform()
# driver.execute_script("window.scrollTo(0, 400);") 
f.close()


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument("--auto-open-devtools-for-tabs")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# amp.scroll()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scrollBy(0, 250)")

# for i in range(20): # adjust integer value for need
#       # you can change right side number for scroll convenience or destination 
#       driver.execute_script("window.scrollBy(0, 250)")
#       # you can change time integer to float or remove
#       time.sleep(1)















# el=driver.find_element_by_xpath('//*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div/div')

# paser = webdriver.common.action_chains.ActionChains(driver)
# paser.move_to_element_with_offset(el, 5, 5)
# paser.click()
# paser.perform()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# elemen = driver.find_element_by_xpath('//*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div/div/div[5]/button')
# actions = ActionChains(driver)
# actions.move_to_element(elemen).perform()

# element = driver.find_element_by_xpath('//*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div')
# driver.execute_script("arguments[0].scrollIntoView(true);", element);
# driver.execute_script("arguments.scrollBy(0,arguments[0].scrollHeight)", element)

# //*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div/div/div[5]/button

# element = driver.find_element_by_xpath('//*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div')# or your another selector here
# action.move_to_element(element)
# action.perform()
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div/div'))).click()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# elementer = driver.find_element_by_xpath('//*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div/div').click

# driver.execute_script("arguments[0].scrollIntoView(true);", elementer);
# print(document.body.scrollHeight)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("window.scrollTo(0, 480)")
time.sleep(10)

# time.sleep(25)
# element = driver.find_element_by_id("my-id")
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()
# ScrollNumber=4
# dates = []
# messages = []
# num_of_posts = 1
# for i in range(1, ScrollNumber):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
#     dates.extend(driver.find_elements_by_xpath('//*[@id="dropWrapper-upload"]/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div/div/div[1]/div[1]/div[1]' + str(num_of_posts) + ']'))
#     # messages.extend(driver.find_elements_by_xpath('(//div[contains(@class, "message-body")])[position()>=' + str(num_of_posts) + ']'))
#     num_of_posts = len(dates)
# print(dates)
# print(num_of_posts)
