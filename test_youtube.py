import time

import pytest
from selenium.webdriver.common.by import By


base_url = 'https://www.youtube.com/'
expected_success_url = "https://www.youtube.com/"


@pytest.mark.parametrize("name", [
    ("SpongeBob")
])
@pytest.mark.youtube_test
def test_youtube_search(browser, name):
    browser.get(base_url)
    browser.find_element(By.NAME, "search_query").click()
    time.sleep(1)
    browser.find_element(By.NAME, "search_query").send_keys(name)
    time.sleep(1)
    browser.find_element(By.ID, "search-icon-legacy").click()
    time.sleep(3)
    browser.find_element(By.ID, "logo-icon").click()
    time.sleep(5)
    assert expected_success_url==browser.current_url
    browser.refresh()






    #assert expected_url == browser.current_url
    #jobtype_dropdown = Select(browser.find_element(By.NAME, "job_type"))
    #jobtype_dropdown.select_by_visible_text("Decorating")
    #browser.find_element(By.NAME, "first_name").send_keys(name)
    #browser.find_element(By.NAME, "last_name").send_keys(lastname)
    #browser.find_element(By.NAME, "phone").send_keys("+7-951-289-75-12")
    #browser.find_element(By.NAME, "email").send_keys("eudvlad@gmail.com")
    #browser.find_element(By.XPATH, "//input[@value = 'Schedule My consultation']").click()
    #assert expected_success_url == browser.current_url