import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", help="Add target language as language=ru or smth like this", default=None)


@pytest.fixture(scope="function")
def browser(request):

    print("\nConfigure language of browser Chrome")
    user_language = request.config.getoption("language")

    if user_language != None:
        print(f"\nBrowser language is {user_language}")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    else:
        raise pytest.UsageError("--language should be en, ru, es, fr, etc.")

    print("\nStart browser Chrome")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser Chrome")
    browser.quit()
