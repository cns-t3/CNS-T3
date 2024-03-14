from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the React application URL
driver.get("http://localhost:3000/search/anthony%20tan")    

try:
    # Wait for profile details to be present and displayed
    profile_name_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "profile-name"))
    )
    assert profile_name_element.is_displayed(), "Profile name is not displayed"

    profile_occupation_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "profile-occupation"))
    )
    assert profile_occupation_element.is_displayed(), "Profile occupation is not displayed"

    profile_dob_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "profile-dob"))
    )
    assert profile_dob_element.is_displayed(), "Profile DOB is not displayed"

    profile_nationality_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "profile-nationality"))
    )
    assert profile_nationality_element.is_displayed(), "Profile nationality is not displayed"

    profile_description_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "profile-description"))
    )
    assert profile_description_element.is_displayed(), "Profile description is not displayed"

except Exception as e:
    print("Profile details test failed:", e)

finally:
    driver.quit()