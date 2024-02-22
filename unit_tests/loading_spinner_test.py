from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost:3000/home")

try:
    # Find search input element make a search
    search_input_element = driver.find_element(By.ID, "large-input")
    search_input_element.send_keys("Anthony Tan")
    search_input_element.send_keys(Keys.RETURN)
    spinner_element = driver.find_element(By.ID, "loading-spinner")
    # Wait for spinner to be present and displayed
    assert spinner_element.is_displayed(), "Spinner is not displayed"
    print("Profile details test passed successfully.")
except Exception as e:
    print("Loading spinner test failed:", e)
finally:
    driver.quit()
