"""__main__.py - Entry point. """

from selenium import webdriver

from seleniumdockerexample.settings import SELENIUM_REMOTE_WEBDRIVER_URL

def main():
    print("main(): starting...")
    print("main(): REMOTE_WEBDRIVER_URL: " + SELENIUM_REMOTE_WEBDRIVER_URL)
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=SELENIUM_REMOTE_WEBDRIVER_URL,
        options=chrome_options
    )
    print("main(): Connected to remote driver.")
    driver.get("https://wikipedia.org")
    title = driver.title;
    print("main(): title: " + title)
    driver.quit()
    print("main(): Driver quited")


if __name__ == "__main__":
    main()
