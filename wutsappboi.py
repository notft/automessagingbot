from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  #this is where u upload ur chrome location
CHROME_PROFILE_PATH = r'C:\Users\aibel\AppData\Local\Google\Chrome\User Data' #make sure u hceck if u have mor than 1 profile
highlyconfidential = "test" #ur test message

chrome_options = Options()
chrome_options.binary_location = CHROME_PATH
chrome_options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get('https://web.whatsapp.com')

    name_buttonlalal = WebDriverWait(driver, 45).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f"span[title='Mynum (You)']"))   #try by driver.find _element() meathod if this arises errors
    )

    name_buttonlalal.click()

    message_box = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10']")
    message_box.send_keys(highlyconfidential)
    message_box.send_keys(Keys.ENTER)



    time.sleep(60)
    print("has been clicked")

finally:
    time.sleep(5)
    driver.quit()