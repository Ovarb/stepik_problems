import time
from selenium.webdriver.common.by import By


def test_add_to_basket_button(browser):
    item_title_expected = "Coders at Work"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(link)
    # pause for visual check
    time.sleep(5)

    #add item to backet
    button_add_to_basket = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    button_add_to_basket.click()

    #go to basket
    button_go_to_basket = browser.find_element(By.XPATH, "//div[contains(@class, 'basket-mini')]//a[contains(@href, 'basket')]")
    button_go_to_basket.click()

    #check item is added to backet
    item_name = browser.find_element(By.XPATH, "//div[contains(@class, 'basket-items')]//div[@class='row']//h3//a")

    assert item_name.text == item_title_expected, f"Expected item's title has to be {item_title_expected}"

