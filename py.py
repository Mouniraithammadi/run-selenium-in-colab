# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # Run in headless mode
selenium_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=selenium_service, options=chrome_options)
driver.get('http://192.168.0.1/')
