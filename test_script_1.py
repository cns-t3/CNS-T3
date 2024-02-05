from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:3001/detailedarticle")  # Replace with the actual URL

wait = WebDriverWait(driver, 10)

# Test Case 1: Article Title
# expected_title = "Cambodian PM Meets Grab's CEO in Davos"
# title = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), '{}')]".format(expected_title))))

expected_title = "Cambodian PM Meets Grab's CEO in Davos"
title = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), \"" + expected_title + "\")]")))
assert title.text == expected_title, f"Title test failed: Expected '{expected_title}', got '{title.text}'"

# Test Case 2: Article Summary
expected_start_summary = "Cambodian Prime Minister Hun Manet met Grab's CEO Anthony Tan"
summary = driver.find_element(By.XPATH, "//p[contains(text(), 'Summary:')]/following-sibling::p")
assert summary.text.startswith(expected_start_summary), "Summary test failed: Summary does not start with expected text"

# Test Case 3: Article Content
expected_content_phrase = "Cambodian Prime Minister Samdech Moha Borvor Thipadei Hun Manet met with Grab's CEO Mr. Anthony Tan"
content = driver.find_element(By.XPATH, "//div[contains(@class, 'border-t')]/p")
assert expected_content_phrase in content.text, "Content test failed: Expected phrase not found in content"

# Test Case 4: Source URL
expected_url = "https://akp.gov.kh/post/detail/296169"
source_url = driver.find_element(By.XPATH, "//a[contains(@href, 'http')]")
assert source_url.get_attribute("href") == expected_url, f"Source URL test failed: Expected URL '{expected_url}', got '{source_url.get_attribute('href')}'"

# Test Case 5: Presence of a Close or Back Button
back_button = driver.find_element(By.XPATH, "//button[./*[name()='svg']]")
assert back_button, "Back button test failed: Back button not found"

print("All tests passed successfully!")

driver.quit()
