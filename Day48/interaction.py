from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")
# number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(number.text)
# number.click()

# Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
# search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
# search.send_keys("Python", Keys.ENTER)
# search.send_keys("Python")

search = driver.find_element(By.NAME, value="fName")
search.send_keys("Dominik", Keys.ENTER)
search = driver.find_element(By.NAME, value="lName")
search.send_keys("Serwatka", Keys.ENTER)
search = driver.find_element(By.NAME, value="email")
search.send_keys("dominik@gmail.com")
sign_button = driver.find_element(By.XPATH, value='/html/body/form/button')
sign_button.click()


