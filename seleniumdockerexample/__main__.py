"""__main__.py - Entry point. """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    # element_to_be_clickable,
    visibility_of,
)

from seleniumdockerexample.settings import SELENIUM_REMOTE_CHROME_WEBDRIVER_URL


def main():
    print("main(): starting...")
    print("main(): REMOTE_WEBDRIVER_URL: " + SELENIUM_REMOTE_CHROME_WEBDRIVER_URL)
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=SELENIUM_REMOTE_CHROME_WEBDRIVER_URL,
        options=chrome_options
    )
    print("main(): Connected to remote driver.")
    driver.get("https://google.com")
    title = driver.title;
    print("main(): title: " + title)
    input_el = WebDriverWait(driver, 20).until(visibility_of(driver.find_element(By.CSS_SELECTOR, 'input[title=Search]')))
    print("main(): input_el: "      + input_el.get_attribute('outerHTML'))
    # search_btn_el = WebDriverWait(driver, 20).until(element_to_be_clickable((By.CSS_SELECTOR, 'input[value="Google Search"]')))
    # print("main(): search_btn_el: " + search_btn_el.get_attribute('outerHTML'))
    input_el.send_keys("Selenium")
    input_el.submit()
    # search_btn_el.click()
    result_el_list = WebDriverWait(driver, timeout=20).until(lambda d: d.find_elements(By.CSS_SELECTOR, 'div[class^="g "]'))
    for el in result_el_list:
        print("main(): result: " + el.get_attribute('innerText'))
    cookies = driver.get_cookies()
    print("main(): cookies: " + str(cookies))
    driver.quit()
    print("main(): Driver quited")


if __name__ == "__main__":
    main()
