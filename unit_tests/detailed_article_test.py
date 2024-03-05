# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("http://localhost:3000/search/tim%20cook")  # Replace with the actual URL
# wait = WebDriverWait(driver, 10)

# try:
#     # Check for the presence of the title
#     title = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Cambodian PM Meets Grab')]")))
#     assert title is not None, "Title not found"
#     print("Title test passed successfully -", title.text)

#     # Check for the presence of the summary
#     summary = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Summary:')]/following-sibling::p")))
#     assert summary.text.startswith("Cambodian Prime Minister Hun Manet met Grab's CEO Anthony Tan"), "Summary does not match expected text"
#     print("Summary test passed successfully -", summary.text)

#     # Check for the presence of the content
#     content = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'border-t')]/p")))
#     assert "Cambodian Prime Minister Samdech Moha Borvor Thipadei Hun Manet met with Grab's CEO Mr. Anthony Tan" in content.text, "Content does not contain expected text"
#     print("Content test passed successfully -", content.text)

#     # Check for the presence of the source URL
#     source_url = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'http')]")))
#     assert "https://akp.gov.kh/post/detail/296169" in source_url.get_attribute("href"), "Source URL does not match expected URL"
#     print("Source URL test passed successfully -", source_url.get_attribute("href"))

# except Exception as e:
#     print("Test failed:", e)

# finally:
#     driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the React application URL
driver.get("http://localhost:3000/search/tim%20cook")

try:
    # Wait for the news article container to be present and displayed
    news_article_container = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "news-article-container"))
    )
    assert news_article_container.is_displayed(), "News article container is not displayed"

    # Validate the presence of each element

    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "article-publisher"))
    ).is_displayed(), "Article publisher is not displayed"

    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "article-title"))
    ).is_displayed(), "Article title is not displayed"

    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "article-tag-hidden"))
    ).is_displayed(), "Article tag (hidden) is not displayed"

    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "article-summary"))
    ).is_displayed(), "Article summary is not displayed"

    print("Presence of each element in the NewsArticle component is validated.")

except Exception as e:
    print("Element presence test failed:", e)

finally:
    driver.quit()
