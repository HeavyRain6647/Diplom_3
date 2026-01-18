from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED_LINK = (By.XPATH, ".//p[text()='Лента Заказов']")
    INGREDIENT_CARD = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")
    MODAL_WINDOW = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    BUN_INGREDIENT = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']")
    BASKET_AREA = (By.CLASS_NAME, "BurgerConstructor_basket__29_qc")
    COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num')]")

class FeedPageLocators:
    ALL_TIME_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]")