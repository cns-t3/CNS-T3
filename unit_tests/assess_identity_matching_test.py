from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time 

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
    
    # Click on the filter button and input 10 for identity match
    filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "filterButton"))
    )
    filter_button.click()
    
    input_field = driver.find_element(By.ID, 'identityMatchFilter')
    input_field.clear()
    input_field.send_keys('10')
        
    apply_button = driver.find_element(By.ID, "applyButton")
    apply_button.click()
    
    time.sleep(5)
    
    try:
        no_articles_element = driver.find_element(By.ID, "noArticles")
        if no_articles_element:
            assert True
    
    except NoSuchElementException:
        # Validate the presence and correctness of the identity matching
        identityMatches = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "identityMatching"))
    )
    # Check if identity matching are displayed
    for identityMatch in identityMatches:
        text = identityMatch.text
        percentage = float(text.strip('%'))
        assert percentage > 10

except Exception as e:
    print("Element presence test failed:", e)

finally:
    driver.quit()