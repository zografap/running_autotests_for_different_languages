import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_cart(browser): 
  browser.get(link)
  time.sleep(5)
  button = browser.find_element_by_css_selector('button.btn-add-to-basket').get_attribute('value')
  assert len(button) > 0, 'Add to cart button not found. (Кнопка добавления в корзину не найдена)'
