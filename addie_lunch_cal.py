from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import re

from selenium import webdriver


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    # URL to acknowledge the terms of use
    url = "https://www.schoolnutritionandfitness.com/webmenus2/#/ocr-pdf?id=64da2310e96f1ed831c544ca"
    
    # Open the URL
    driver.get(url)
    time.sleep(5)

    acknowledge_button = driver.find_element(By.CLASS_NAME, "btn.btn-default.pull-right")

    # Click the acknowledge button to accept the terms of use
    acknowledge_button.click()
    time.sleep(5)
    # Optionally, you can wait for a few seconds to allow the page to load
    #driver.implicitly_wait(50)

    elements = driver.find_elements(By.XPATH, "//div[@tabindex=0]")

    # Create an empty list to store the text from elements
    h3_texts = []
    menu_items = []
   
    # Loop through each h3 element and store ibts text in the list
    for element in elements:

        date = element.find_element(By.CLASS_NAME, "menuday").text
        date = date.replace('Menu:', '')
        print (date)
        menu = element.find_element(By.CLASS_NAME, "sc-cSHVUG.fyanpg").text
        menu =re.sub("\(.*?\)","()",menu)
        menu = menu.replace('(','')
        menu = menu.replace(')','')
        menu = menu.replace('\n\n', '\n')
        menu = menu.replace('\n\n', '\n')
        print (menu)


finally:
    # Close the WebDriver
    driver.quit()

