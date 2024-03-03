from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    # Open the search page
    driver.get("http://localhost:3000/search/anthony%20tan")

    # Click the logo link using its ID
    logo_link = driver.find_element(By.ID, "logoLink")
    logo_link.click()

    # Wait for the navigation to complete
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost:3000/home"))

    # Verify that the current URL is the homepage
    current_url = driver.current_url
    assert current_url == "http://localhost:3000/home", "Navigation to homepage failed"
    print("Logo navigation test passed successfully.")

except Exception as e:
    print("Logo navigation test failed:", e)

finally:
    driver.quit()