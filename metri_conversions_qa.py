from selenium import webdriver
import pytest
import time

link = 'https://www.metric-conversions.org/'


def celsius_to_fahrenheit():
    browser = webdriver.Chrome()
    browser.get(link)

    celc_field = browser.find_element_by_id("queryFrom")
    celc_field.send_keys('Celsius')
    time.sleep(2)

    fahr_field = browser.find_element_by_id("queryTo")
    fahr_field.send_keys('Fahrenheit')
    time.sleep(2)

    warning_button = browser.find_element_by_class_name("convert.greenButton")
    warning_button.click()
    time.sleep(2)

    field_for_input = browser.find_element_by_id('argumentConv')
    field_for_input.send_keys('40')
    time.sleep(4)
    browser.quit()


def meters_to_feet():
    browser = webdriver.Chrome()
    browser.get(link)
    category_button = browser.find_element_by_class_name('typeConv.length.bluebg')
    category_button.click()
    time.sleep(3)
    button2 = browser.find_element_by_css_selector("div#popLinks ol li:first-child")
    browser.execute_script("window.scrollBy(0, 150);")
    time.sleep(3)
    button2.click()
    time.sleep(3)
    browser.quit()


def ounces_to_grams():
    browser = webdriver.Chrome()
    browser.get(link)
    category_button = browser.find_element_by_class_name('typeConv.weight.bluebg')
    category_button.click()
    time.sleep(3)
    button2 = browser.find_element_by_link_text('Ounces to Grams')
    browser.execute_script("window.scrollBy(0, 200);")
    time.sleep(3)
    button2.click()
    finall_field = browser.find_element_by_id('argumentConv')
    time.sleep(3)
    finall_field.send_keys('5')
    time.sleep(10)
    browser.quit()
