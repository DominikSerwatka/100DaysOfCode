from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
LINKEDIN_URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3784827676&f_AL=true&geoId=105072130&keywords=Python%20Developer&location=Polska&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true'
PASSWORD = os.environ['PASSWORD']
EMAIL = os.environ['EMAIL']
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(LINKEDIN_URL)
time.sleep(3)
button_one = driver.find_element(By.XPATH, value='//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[1]')
button_one.click()
# time.sleep(2)
# button_two = driver.find_element(By.XPATH, value='//*[@id="close-small"]/path')
# button_two.click()
time.sleep(3)
login = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
login.click()
time.sleep(3)
email = driver.find_element(By.ID, value='username')
email.send_keys(EMAIL)
password = driver.find_element(By.ID, value='password')
password.send_keys(PASSWORD)
login_enter = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
login_enter.click()
time.sleep(6)

button_three = driver.find_element(By.XPATH, value='//*[@id="ember41"]')
button_three.click()

time.sleep(3)
jobs = driver.find_elements(By.CSS_SELECTOR, value=".scaffold-layout__list-container li div a")
for n in range(0, 5):
    jobs[n].click()
    time.sleep(2)
    save = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')
    save.click()
    time.sleep(2)
    follow = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div/div[2]/div/div[1]/div/section/section/div[1]/div[1]/button')
    to_scroll = driver.find_element(By.XPATH, value='//*[@id="how-you-match-card-container"]/section[3]')
    driver.execute_script("arguments[0].scrollIntoView();", to_scroll)
    time.sleep(2)
    follow.click()
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView();", jobs[n+1])
