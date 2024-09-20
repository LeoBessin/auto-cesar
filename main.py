from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(service=service,options=options)

def is_connected():
    try:
        driver.find_element(By.ID, "header")
        return True
    except:
        return False
        raise

try:
    # Navigate to a website
    driver.get("https://cesar.emineo-informatique.fr/")

    # Print the title of the page
    print(driver.title)

    # Find an element and interact with it (example: search box)
    if not is_connected():
        print('Not connected')
        loginBox = driver.find_element(By.ID, "username")
        passwordBox = driver.find_element(By.ID, "password")
        loginBox.send_keys(login)
        passwordBox.send_keys(password)
        passwordBox.send_keys(Keys.RETURN)

    # Wait for a few seconds to see the results
    driver.implicitly_wait(1000)

finally:
    # Close the browser
    ...
    while True:
        pass
    driver.quit()

