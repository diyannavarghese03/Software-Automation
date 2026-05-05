from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 1. Setup Firefox
dv = webdriver.Firefox()
dv.maximize_window()

# Set a timeout limit (e.g., 10 seconds)
wait = WebDriverWait(dv, 10)

try:
    # 2. Open the Website
    print("Navigating to site...")
    dv.get("https://the-internet.herokuapp.com/login")

    # 3. Wait for elements to exist before typing (Prevents "NoSuchElementException")
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_field = dv.find_element(By.ID, "password")
    login_button = dv.find_element(By.CSS_SELECTOR, "button.radius")

    # 4. Perform Login
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")
    login_button.click()

    # 5. Navigation Check: Wait for the Success Message or Dashboard URL
    wait.until(EC.url_contains("/secure"))
    print("Login Successful! Navigated to Secure Area.")

    # 6. Further Navigation: Click a 'Logout' or 'Home' link
    logout_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
    logout_btn.click()
    print("Navigation Successful: Logged out.")

except TimeoutException:
    print("Error: The page took too long to load or an element wasn't found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # 7. Close browser safely
    print("Closing browser...")
    driver.quit()
