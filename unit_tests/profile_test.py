from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the React application URL
driver.get("http://localhost:3000/search/tim%20cook")    

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

    # Validate profile details text based on the provided data
    assert profile_name_element.text == "Tim Cook", f"Expected name: Tim Cook, Actual name: {profile_name_element.text}"
    assert profile_occupation_element.text == "CEO, at Apple Inc.", f"Expected occupation: CEO, at Apple Inc., Actual occupation: {profile_occupation_element.text}"
    assert profile_dob_element.text.startswith("Born: 1 Nov 1960"), f"DOB format mismatch"
    assert profile_nationality_element.text == "Nationality: American", f"Expected nationality: American, Actual nationality: {profile_nationality_element.text}"
    assert profile_description_element.text.startswith("Tim Cook is a distinguished business leader"), f"Description mismatch"

    print("Profile details test passed successfully.")

except Exception as e:
    print("Profile details test failed:", e)

finally:
    driver.quit()