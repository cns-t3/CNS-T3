from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time 
from datetime import datetime, timedelta

# Helper function to check if a date falls within the past 7 days
def is_within_past_7_days(date_str, date_format="%d-%b-%Y"):
    today = datetime.now()
    date_to_check = datetime.strptime(date_str, date_format)
    seven_days_ago = today - timedelta(days=30)
    return seven_days_ago <= date_to_check <= today

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the React application URL
driver.get("http://localhost:3000/search/1/Anthony%20Tan")

try:
    # Wait for the news article container to be present and displayed
    news_article_container = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.ID, "news-articles-container"))
    )
    assert len(news_article_container) > 0, "News articles container is not displayed"
    
    # Click on the filter button and click on "past 7 days"
    filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "filterButton"))
    )
    filter_button.click()
    
    # Click on the date filter button
    date_filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "dateFilterButton"))
    )
    date_filter_button.click()
    
    dateOption = driver.find_element(By.ID, "past 30 days")
    dateOption.click()
        
    apply_button = driver.find_element(By.ID, "applyButton")
    apply_button.click()
    
    time.sleep(5)
    
    try:
        no_articles_element = driver.find_element(By.ID, "noArticles")
        if no_articles_element:
            assert True
    
    except NoSuchElementException:
        dates_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "date"))
        )
        
        # Check if dates are displayed and within the past 7 days
        for element in dates_elements:
            date_text = element.text.replace(" ", "-")
            if not is_within_past_7_days(date_text):
                assert False
            else:
                assert True

except Exception as e:
    print("Element presence test failed:", e)

finally:
    driver.quit()
