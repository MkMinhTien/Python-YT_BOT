import os
from selenium import webdriver
from time import sleep

driver = webdriver.ChromeOptions()
driver.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver.add_argument("--headless")
driver.add_argument("--no-sandbox")
driver.add_argument("--disable-dev-shm-usage")

driver1 = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=driver)
driver2 = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=driver)
driver3 = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=driver)
driver4 = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=driver)
driver5 = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=driver)

driver1.get("https://www.youtube.com/watch?v=ZpdQyMQzrtk")
driver2.get("https://www.youtube.com/watch?v=ZpdQyMQzrtk")
driver3.get("https://www.youtube.com/watch?v=ZpdQyMQzrtk")
driver4.get("https://www.youtube.com/watch?v=ZpdQyMQzrtk")
driver5.get("https://www.youtube.com/watch?v=ZpdQyMQzrtk")

while True:
    sleep(25)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()
    driver5.refresh()
