from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Firefox()


def openPage() :
    browser.get("http://localhost:8080/ship-manage/login")
    browser.find_element_by_id("name").send_keys("admin")
    browser.find_element_by_id("pass").send_keys("123123")
    browser.find_element_by_class_name("btn").click()

    locator = (By.ID, 'frontMain')

    WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located(locator))

    browser.get("http://localhost:8080/ship-manage/ship/component/shipComponent/index2");
    browser.find_element_by_id("shipComponent2_add").click()

    browser.find_element_by_id("edit_componentCname").send_keys("1")

    browser.find_element_by_id("categoryOrParent").click()
    browser.find_element_by_id("A2431C34-1C12-4A17-8189-8B93926EB3A4").click()
    browser.find_element_by_id("edit_componentModel").send_keys("2")

    browser.find_element_by_id("edit_manufacturer").send_keys("3")
    browser.find_element_by_id("edit_cwbtCode").send_keys("AA-000-000-000")
    # js="document.getElementById('componentType_id').style.display='block';"
    # browser.execute_script(js)
    browser.find_element_by_class_name("btn-group")

    Select(browser.find_element_by_id("componentType_id")).select_by_value("E25F1252-577F-44B8-B280-6A60C62504E0")
    Select(browser.find_element_by_id("post_id")).select_by_value("413936AB-970D-4CFB-B05C-BA88F4C869E0")

    browser.find_element_by_id("shipComponent_save").click()
    # browser.find_element_by_id('su').click()

    # print(browser.page_source)

    # browser.close()


openPage()