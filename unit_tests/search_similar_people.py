from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the React application URL
driver.get("http://localhost:3000/")

try:
    large_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'large-input'))
    )
    
    large_input.send_keys('Anthoni Tan')
    large_input.send_keys(Keys.ENTER)
    
    similar_people_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'similarPeople'))
    )
    
    similar_people_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'similarPeople'))
    )
    
    if similar_people_elements:
        # Click on the first element of the list
        similar_people_elements[0].click()
    else:
        print("No elements found with class 'similarPeople'.")
        
    WebDriverWait(driver, 10).until(EC.url_contains("/search/1/Anthony%20Tan"))
    expected_url = "http://localhost:3000/search/1/Anthony%20Tan"
    assert driver.current_url == expected_url

except TimeoutException:
    print("Timed out waiting for elements to be present.")

finally:
    driver.quit()
