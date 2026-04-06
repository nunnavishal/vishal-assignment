from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdNabuAutomation:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def open_site(self):
        self.driver.get("https://adnabu-store-assignment1.myshopify.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID,"password").send_keys("AdNabuQA")
        self.driver.find_element(By.XPATH,"//button[text()='Enter']").click()

    def search_product(self, product_name):
        search_icon = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "summary[aria-label='Search']"))
        )
        search_icon.click()

        search_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.ENTER)

    def select_first_product(self):
        products = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, "h3[id*='title']>a[href*='/products/']")
            )
        )

        self.wait.until(EC.element_to_be_clickable(products[0])).click()

    def add_to_cart(self):
        add_to_cart_btn = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "add"))
        )
        add_to_cart_btn.click()

    def go_to_cart_and_verify(self):
        cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cart']"))
        )
        cart_button.click()

        cart_item = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "cart-item, .cart-item"))
        )

        assert cart_item.is_displayed(), "Product not added to cart"
        print("Product successfully added to cart")
        self.driver.save_screenshot(r"C:\Users\abdul\PycharmProjects\AdNabu_Assignment\Screenshot\test_result5.png")

    def close_browser(self):
        self.driver.quit()


if __name__ == "__main__":
    test = AdNabuAutomation()
    test.open_site()
    test.search_product("The Collection Snowboard: Oxygen")
    test.select_first_product()
    test.add_to_cart()
    test.go_to_cart_and_verify()
    test.close_browser()