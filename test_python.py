from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:3001/detailedarticle")  # Replace with the actual URL

wait = WebDriverWait(driver, 10)

# Check for the presence of the title
title = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Cambodian PM Meets Grab')]")))

# Check for the presence of the summary
summary = driver.find_element(By.XPATH, "//p[contains(text(), 'Summary:')]/following-sibling::p")

# Check for the presence of the content
content = driver.find_element(By.XPATH, "//div[contains(@class, 'border-t')]/p")

# Check for the presence of the source URL
source_url = driver.find_element(By.XPATH, "//a[contains(@href, 'http')]")

# Assertions
assert title is not None
assert summary.text.startswith("Cambodian Prime Minister Hun Manet met Grab's CEO Anthony Tan")
assert "Cambodian Prime Minister Samdech Moha Borvor Thipadei Hun Manet met with Grab's CEO Mr. Anthony Tan" in content.text
assert "https://akp.gov.kh/post/detail/296169" in source_url.get_attribute("href")

driver.quit()
