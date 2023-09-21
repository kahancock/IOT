from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

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

    # Find all h3 elements on the page
    h3_elements = driver.find_elements(By.CLASS_NAME, "menuday")
    menu_elements = driver.find_elements(By.CLASS_NAME, "sc-cSHVUG.fyanpg")

    # Create an empty list to store the text from elements
    h3_texts = []
    menu_items = []
   
    # Loop through each h3 element and store its text in the list
    for h3 in h3_elements:
        date = h3.text
        date = date.replace('Menu:', '')
        h3_texts.append(date)
        print (date)
        print ((h3.find_element(By.CLASS_NAME, ".sc-cSHVUG.fyanpg")).text)

    #for menu in menu_elements:
    #    menu_items.append(menu.text)

    #print(h3_texts)
    #print(menu_items)

finally:
    # Close the WebDriver
    driver.quit()

