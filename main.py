from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from PIL import Image
import time
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("user-data-dir=C:\\Users\\Micha\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directory=Default")

# Set up the WebDriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome(options=options)

# Open the browser and navigate to the book link
driver.get("https://www.everand.com/read/786666967/A-Promised-Land#")

time.sleep(20)  # Adjust the sleep time as needed

# Take screenshots and navigate through pages
i = 1
while True:
    screenshot = driver.get_screenshot_as_png()
    img = Image.open(screenshot)
    img.save(f"page_{i}.png")
    i += 1
    next_button = driver.find_element_by_xpath("//button[@aria-label='Next']")
    next_button.click()
    time.sleep(1)  # Adjust the sleep time as needed

    # Check if there are more pages
    if not next_button.is_displayed():
        break

driver.quit()

# Combine the screenshots into an ePub file (this part requires additional steps)
# You can use libraries like `ebooklib` to create an ePub file
