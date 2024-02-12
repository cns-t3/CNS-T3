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
        EC.presence_of_all_elements_located((By.ID, "news-articles-container"))
    )
    assert len(news_article_container) > 0, "News articles container is not displayed"

    # Validate the presence and correctness of the risk rating
    risk_ratings = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "riskRating"))
    )
    
    # Check if risk ratings are displayed and match the expected values
    for risk_rating in risk_ratings:
        text = risk_rating.text.upper()
        assert text in ["LOW", "MEDIUM", "HIGH"]

except Exception as e:
    print("Element presence test failed:", e)

finally:
    driver.quit()
