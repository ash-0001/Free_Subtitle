from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then
#invoke actual browser
driver = webdriver.Chrome(executable_path=r".\chromedriver_win32\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
#to refresh the browser
driver.refresh()
# identifying the source element
source= driver.find_element_by_xpath("//*[text()='Company']");
# action chain object creation
action = ActionChains(driver)
# move to the element and click then perform the operation
action.move_to_element(source).click().perform()
#to close the browser
driver.close()