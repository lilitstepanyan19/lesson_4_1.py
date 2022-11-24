
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose your language: ')
    
@pytest.fixture(scope='function')    
def browser(request):
    browser = None
    user_language = request.config.getoption('language')

    options = Options()

    options.add_argument('headless')
    options.add_argument('window-size=1920x935')
    
    options.add_experimental_option('prefs', {'intl.accept_language' : user_language})
    if user_language:
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("Enter your language")
    yield browser
    browser.quit()    
        
        