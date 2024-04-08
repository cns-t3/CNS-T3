from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  
driver.implicitly_wait(10)

# Open the React application URL
driver.get("http://localhost:3000/")

try:
    search_input = driver.find_element(By.ID, "large-input")
    search_input.clear()
    # Type the search query
    search_input.send_keys("test")
    # Press Enter to trigger the search
    search_input.send_keys(Keys.RETURN)
    # Wait for search results to load (adjust this according to your app)
    time.sleep(2)

    # Validate redirection
    expected_url = "http://localhost:3000/search/test"
    current_url = driver.current_url
    assert (
        current_url == expected_url
    ), f"Redirection failed. Expected URL: {expected_url}, Actual URL: {current_url}"
    print("Redirection test passed successfully.")

except Exception as e:
    print("Redirection test failed:", e)

finally:
    driver.quit()
