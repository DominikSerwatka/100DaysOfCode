from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TWITTER_EMAIL = 'your_twitter_email'
TWITTER_PASSWORD = 'your_twitter_password'
TWITTER_NAME = 'your_twitter_name'
DOWN = 100
UP = 100


class InternetSpeedTwitterBot:
    def __init__(self, ):
        self.down = 0
        self.up = 0
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(4)
        accept = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        accept.click()
        time.sleep(2)
        go = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(45)
        close = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
        close.click()
        time.sleep(3)
        download = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = float(download)
        upload = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = float(upload)
        if self.up < UP or self.down < DOWN:
            return True
        else:
            return False

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')
        time.sleep(3)
        accept = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]')
        accept.click()
        login = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
        login.click()
        time.sleep(3)
        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        next = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next.click()
        time.sleep(2)
        name = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        name.send_keys(TWITTER_NAME)
        next_2 = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        next_2.click()
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        login_2 = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_2.click()
        time.sleep(7)
        tweet_text = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet_text.send_keys(f'My internet speed is {self.down}down/{self.up}up.')
        post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        post.click()


bot = InternetSpeedTwitterBot()
if bot.get_internet_speed():
    bot.tweet_at_provider()