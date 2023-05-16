import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_link(browser):
    browser.get(link)
    basket_selector = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert basket_selector.text == "Añadir al carrito", 'ошибка ебучая'