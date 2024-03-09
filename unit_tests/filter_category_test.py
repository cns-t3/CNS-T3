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
    
    # Click on the filter button and untick on "Source Of Wealth" and "Family Circumstances" options
    filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "filterButton"))
    )
    filter_button.click()
    
    wealth_checkbox = driver.find_element(By.XPATH, "//input[@value='source of wealth']")
    if wealth_checkbox.is_selected():
        wealth_checkbox.click()
        
    family_checkbox = driver.find_element(By.XPATH, "//input[@value='family circumstances']")
    if family_checkbox.is_selected():
        family_checkbox.click()
        
    apply_button = driver.find_element(By.ID, "applyButton")
    apply_button.click()
    
    time.sleep(5)
    
    try:
        no_articles_element = driver.find_element(By.ID, "noArticles")
        if no_articles_element:
            assert True
    
    except NoSuchElementException:
        # Validate the presence and correctness of the category
        categories = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "category"))
    )
    # Check if category are displayed and match the expected values
    for category in categories:
        text = category.text
        assert text in ["Sensitive Industries", "Sanctioned Countries", "Others"]

except Exception as e:
    print("Element presence test failed:", e)

finally:
    driver.quit()
