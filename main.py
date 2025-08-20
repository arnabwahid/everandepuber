import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import time
from io import BytesIO

# Set up Chrome options for macOS
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("user-data-dir=/Users/dracula/Documents/ChromeUserData")
options.add_argument("profile-directory=Default")

try:
    # Set up the WebDriver (ensure chromedriver is in your PATH)
    driver = webdriver.Chrome(options=options)

    # Create screenshots directory if it doesn't exist
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Open the browser and navigate to the book link
    driver.get(
        "https://www.everand.com/read/385751180/A-Study-Guide-for-Robert-A-Heinlein-s-Stranger-in-a-Strange-Land")
    time.sleep(15)  # Wait for manual login or page load

    wait = WebDriverWait(driver, 15)
    i = 1
    while True:
        # Take screenshot
        screenshot = driver.get_screenshot_as_png()
        img = Image.open(BytesIO(screenshot))
        img.save(f"screenshots/page_{i}.png")
        print(f"Saved page {i}")
        i += 1

        # Try to click the next page arrow
        try:
            next_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "icon.page_arrow.icon-ic_right_arrow"))
            )
            next_button.click()
            # Wait 3 seconds after clicking next before taking the next screenshot
            time.sleep(2)
        except Exception as e:
            print("Next button not found or not clickable. Assuming last page.")
            break

        # Check the page counter to see if it's the last page
        try:
            page_counter = wait.until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "page_counter"))
            ).text
            # Example format: "Page 5 of 10"
            numbers = [int(s) for s in page_counter.split() if s.isdigit()]
            if len(numbers) == 2:
                current_page, total_pages = numbers
                if current_page == total_pages:
                    print("Reached the last page")
                    break
        except Exception as e:
            print("Could not read page counter. Stopping.")
            break

except Exception as main_e:
    print(f"Error: {main_e}")
finally:
    try:
        driver.quit()
    except Exception:
        pass
# ...existing code...
# >>> TBC

# Combine the screenshots into an ePub file (this part requires additional steps)
# You can use libraries like `ebooklib` to create an ePub file


# function that checks if the page is the last one if not it will keep going, once at 100% it will stop
# and continue with script (also one that makes sure you start on the first page)
