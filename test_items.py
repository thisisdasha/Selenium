link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language_and_add_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button, "No button on this website"