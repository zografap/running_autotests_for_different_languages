import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='"chrome" or "firefox".')
    parser.addoption('--language', action='store', default='ru', help='Choose language: ar ca cs da de el en es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb')
    # parser.addoption('--timeout', action='store', default=10, help='Choose timeout time (seconds)')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    # languages = ['ar', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans', 'en-gb']
    # language = request.config.getoption('language')
    language = request.config.getoption('language')

    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(executable_path=r"c://chromedriver//chromedriver.exe")
        browser.implicitly_wait(5)
    
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(5)

    else:
        print(f'\nBrowser "{browser_name}"" is not implemented. "chrome" and "firefox" only')

    yield browser
    browser.quit()
