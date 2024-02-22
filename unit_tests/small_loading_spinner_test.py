from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost:3000/search/test")

try:
    # Find search input element make a search
    search_input_element = driver.find_element(By.ID, "small-input")
    search_input_element.send_keys("Anthony Tan")
    search_input_element.send_keys(Keys.RETURN)
    spinner_element = driver.find_element(By.ID, "loading-spinner")
    # Wait for spinner to be present and displayed
    assert spinner_element.is_displayed(), "Spinner is not displayed"
    print("Small loading spinner test passed successfully.")
except Exception as e:
    print("Loading spinner test failed:", e)
finally:
    driver.quit()
