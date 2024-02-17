from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:3000/detailedarticle")  # Replace with the actual URL
wait = WebDriverWait(driver, 10)

try:
    # Check for the presence of the title
    title = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Cambodian PM Meets Grab')]")))
    assert title is not None, "Title not found"
    print("Title test passed successfully -", title.text)

    # Check for the presence of the summary
    summary = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Summary:')]/following-sibling::p")))
    assert summary.text.startswith("Cambodian Prime Minister Hun Manet met Grab's CEO Anthony Tan"), "Summary does not match expected text"
    print("Summary test passed successfully -", summary.text)

    # Check for the presence of the content
    content = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'border-t')]/p")))
    assert "Cambodian Prime Minister Samdech Moha Borvor Thipadei Hun Manet met with Grab's CEO Mr. Anthony Tan" in content.text, "Content does not contain expected text"
    print("Content test passed successfully -", content.text)

    # Check for the presence of the source URL
    source_url = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'http')]")))
    assert "https://akp.gov.kh/post/detail/296169" in source_url.get_attribute("href"), "Source URL does not match expected URL"
    print("Source URL test passed successfully -", source_url.get_attribute("href"))

except Exception as e:
    print("Test failed:", e)

finally:
    driver.quit()
