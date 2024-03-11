from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime


def string_to_date(date_str):
    return datetime.strptime(date_str.text.replace(" ", "-"), "%d-%b-%Y")


def check_newest_first(arr_date_str):
    for i in range(len(arr_date_str) - 1):
        if string_to_date(arr_date_str[i]) < string_to_date(arr_date_str[i + 1]):
            return False
    return True


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

    sort_by_date_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "sortByDateButton"))
    )
    sort_by_date_button.click()

    date_drop_down_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "dateDropDownButton"))
    )

    date_drop_down_button.click()

    oldest_to_newest = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "Oldest to Newest"))
    )

    oldest_to_newest.click()

    try:
        no_articles_element = driver.find_element(By.ID, "noArticles")
        if no_articles_element:
            assert True

    except NoSuchElementException:
        dates_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "date"))
        )

        # Check if dates are displayed from newest to oldest
        if not check_newest_first(dates_elements):
            assert True
        else:
            assert False

except Exception as e:
    print("Element presence test failed:", e)

finally:
    driver.quit()
