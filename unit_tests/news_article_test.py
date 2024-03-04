from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the React application URL
driver.get("http://localhost:3000/search/anthony%20tan")

try:
    # Wait for the news article container to be present and displayed
    news_article_container = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "news-article-container"))
    )
    assert (
        news_article_container.is_displayed()
    ), "News article container is not displayed"

    # Validate the presence of each element

    assert (
        WebDriverWait(driver, 10)
        .until(EC.presence_of_element_located((By.ID, "article-publisher")))
        .is_displayed()
    ), "Article publisher is not displayed"

    assert (
        WebDriverWait(driver, 10)
        .until(EC.presence_of_element_located((By.ID, "article-title")))
        .is_displayed()
    ), "Article title is not displayed"

    assert (
        WebDriverWait(driver, 10)
        .until(EC.presence_of_element_located((By.ID, "article-summary")))
        .is_displayed()
    ), "Article summary is not displayed"

    assert (
        WebDriverWait(driver, 10)
        .until(EC.presence_of_element_located((By.ID, "category")))
        .is_displayed()
    ), "Category is not displayed"

    print("Presence of each element in the NewsArticle component is validated.")

except Exception as e:
    print("Element presence test failed:", e)

finally:
    driver.quit()
