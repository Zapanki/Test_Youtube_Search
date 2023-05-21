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





