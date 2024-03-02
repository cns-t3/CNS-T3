from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time 

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the React application URL
driver.get("http://localhost:3000/search/anthony%20tan")

try:
    # Wait for the news article container to be present and displayed
    news_article_container = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.ID, "news-articles-container"))
    )
    assert len(news_article_container) > 0, "News articles container is not displayed"
    
    # Click on the filter button and click on "Low" and "High" options
    filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "filterButton"))
    )
    filter_button.click()
    
    high_risk_checkbox = driver.find_element(By.XPATH, "//input[@value='high']")
    if not high_risk_checkbox.is_selected():
        high_risk_checkbox.click()
    
    med_risk_checkbox = driver.find_element(By.XPATH, "//input[@value='medium']")
    if med_risk_checkbox.is_selected():
        med_risk_checkbox.click()
        
    low_risk_checkbox = driver.find_element(By.XPATH, "//input[@value='low']")
    if not low_risk_checkbox.is_selected():
        low_risk_checkbox.click()
        
    apply_button = driver.find_element(By.ID, "applyButton")
    apply_button.click()
    
    time.sleep(5)
    
    try:
        no_articles_element = driver.find_element(By.ID, "noArticles")
        if no_articles_element:
            assert True
    
    except NoSuchElementException:

        # Validate the presence and correctness of the risk rating
        risk_ratings = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "riskRating"))
        )
        
        # Check if risk ratings are displayed and match the expected values
        for risk_rating in risk_ratings:
            text = risk_rating.text.upper()
            assert text in ["LOW", "HIGH"]

except Exception as e:
    print("Element presence test failed:", e)

finally:
    driver.quit()
