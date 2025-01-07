import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import time
from io import BytesIO
import pytesseract
from ebooklib import epub
'''
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("user-data-dir=C:\\Users\\Micha\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directory=Default")

# Set up the WebDriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome(options=options)

# Create screenshots directory if it doesn't exist
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Open the browser and navigate to the book link
driver.get("https://www.everand.com/read/786666967/A-Promised-Land#")

time.sleep(15)

# Take screenshots and navigate through pages
wait = WebDriverWait(driver, 10)
i = 1
while True:
    screenshot = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(screenshot))
    img.save(f"screenshots/page_{i}.png")
    i += 1

    # Wait for the right arrow to be clickable and click it
    next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon.page_arrow.icon-ic_right_arrow")))
    next_button.click()

    # Check the page counter to see if it's the last page
    page_counter = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page_counter"))).text
    current_page, total_pages = map(int, page_counter.split()[1::2])
    if current_page == total_pages:
        print("Reached the last page")
        break

driver.quit()
'''
# ...existing code...


# Combine the screenshots into an ePub file (this part requires additional steps)
# You can use libraries like `ebooklib` to create an ePub file





# function that checks if the page is the last one if not it will keep going, once at 100% it will stop
# and continue with script (also one that makes sure you start on the first page)