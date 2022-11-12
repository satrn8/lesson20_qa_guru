import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser


@allure.tag('mobile')
@allure.title('Search Wiki')
def test_search_wiki():
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('BrowserStack')
    browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).should(have.size_greater_than(0))


@allure.tag('mobile')
@allure.title('Test search')
def test_open_wiki():
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Quality assurance")
    browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).should(have.size_greater_than(0))


