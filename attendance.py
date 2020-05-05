print("Starting to run")
import requests
import pyautogui
import webbrowser
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import schedule
def repeat():
	driver = webdriver.Firefox()
	driver.maximize_window()
	driver.get('https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&followup=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
	print('Going to classroom')
	email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
	#THIS IS WHERE YOU PUT YOUR EMAIL
	email_phone.send_keys("PUT EMAIL HERE")
	driver.find_element_by_id("identifierNext").click()
	password = WebDriverWait(driver, 10).until(
	    EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
	)
	#THIS IS WHERE YOU PUT YOUR PASSWORD
	password.send_keys("PUT PASSWORD HERE")
	driver.find_element_by_id("passwordNext").click()
	print('Logged in!')
	time.sleep(7)
	####Above is to get to classroom
	print('Going to attandance class')
	driver.find_element_by_xpath("//ol//div[contains(text(),'SFP Attendance')]").click()
	time.sleep(3)
	print('Going to attandance tab')
	driver.find_element_by_xpath("//html//body//div//div//div//aside//div//div//div//div//div//a[contains(text(),'Attendance')]").click()
	time.sleep(2)
	print('Turning in attendance!')
	driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/aside/div[1]/div[2]/div[2]/span/label[1]/span").click()
	time.sleep(2)
	driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/aside/div[1]/div[2]/div[3]/div/span").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div[12]/div/div[2]/div[3]/div[2]/span/span").click()
	print("Attendance turned in!")
	time.sleep(5)	
	driver.close()
schedule.every().monday.at("03:32").do(repeat)
schedule.every().tuesday.at("01:13").do(repeat)
schedule.every().wednesday.at("03:10").do(repeat)
schedule.every().thursday.at("03:10").do(repeat)

while True:
    schedule.run_pending()
    time.sleep(2)
