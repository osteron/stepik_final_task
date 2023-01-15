import pytest
from selenium import webdriver

# Список всех доступных локализаций для дальнейшего сравнения с передаваемым параметром
localizations = ['ar', 'ca', 'cs', 'da', 'de', 'en', 'el', 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl', 'pt', 'pt-br',
                 'ro', 'ru', 'sk', 'uk', 'zh-cn']

# Список всех доступных браузеров для дальнейшего сравнения с передаваемым параметром
browsers = ['chrome', 'firefox']


def pytest_addoption(parser):
    # По умолчанию установлен браузер chrome - в задании сказано, что достаточно проверить только на нем,
    # но при этом существует возможность указать в параметре браузер firefox
    parser.addoption('--browser_name', action='store', default=browsers[0],
                     help='Choose browser: chrome or firefox')
    # По умолчанию локализация установлена в None
    parser.addoption('--language', action='store', default='en',
                     help=f'Choose language: {localizations}')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    user_language = request.config.getoption('language')

    # Если параметр --language является None
    if not user_language:
        raise pytest.UsageError(f'--language should be {localizations}')
    # Если параметр --language содержит невалидное значение локализации
    elif user_language.lower() not in localizations:
        raise pytest.UsageError(f'--language={user_language} -> should be {localizations}')

    if browser_name.lower() == 'chrome':
        print('\nstart chrome browser fot test..')
        options = webdriver.chrome.options.Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument("--incognito")
        browser = webdriver.Chrome(options=options)
    elif browser_name.lower() == 'firefox':
        print('\nstart firefox browser for test..')
        options = webdriver.firefox.options.Options()
        options.set_preference("intl.accept_languages", user_language)
        options.add_argument("--private")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError(f'--browser_name should be {browsers}')
    yield browser
    print('\nquit browser..')
    browser.quit()
