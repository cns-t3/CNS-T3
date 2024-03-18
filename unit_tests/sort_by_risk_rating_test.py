from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime


def string_to_date(date_str):
    return datetime.strptime(date_str.text.replace(" ", "-"), "%d-%b-%Y")


def check_order(arr_str, asc=True):
    if asc:
        return all(arr_str[i] <= arr_str[i+1] for i in range(len(arr_str) - 1))
    else:
        return all(arr_str[i] >= arr_str[i+1] for i in range(len(arr_str) - 1))


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

    # Click on the sort button
    sort_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "sortByButton"))
    )
    sort_button.click()

    # Click on the dropdown
    risk_dropdown_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "dropDownButton"))
    )
    risk_dropdown_button.click()

    # Click on the High to Low option
    high_to_low = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "High Risk to Low Risk"))
    )
    high_to_low.click()

    try:
        # Check if there are no articles message is displayed
        no_articles_element = driver.find_element(By.ID, "noArticles")
        if no_articles_element:
            assert True

    except NoSuchElementException:
        # Check if risk ratings are displayed in the correct order (High to Low)
        risk_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "riskRating"))
        )
        risk_ratings = [elem.text for elem in risk_elements]
        assert check_order(risk_ratings, asc=False), "Risk ratings are not sorted correctly"

except Exception as e:
    print("Test failed:", e)

finally:
    driver.quit()