from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_FIELD_NAME = By.XPATH, '//*[@placeholder="* Имя"]'  # Поле "Имя"

    INPUT_FIELD_SURNAME = By.XPATH, '//*[@placeholder="* Фамилия"]'  # Поле "Фамилия"

    INPUT_FIELD_ADDRESS = By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]'  # Поле "Адрес"

    INPUT_FIELD_METRO_STATION = By.XPATH, '//*[@placeholder="* Станция метро"]'  # Поле "Станция метро"

    INPUT_FIELD_PHONE = By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]'  # Поле "Телефон"

    INPUT_FIELD_DATE = By.XPATH, '//*[@placeholder="* Когда привезти самокат"]'  # Поле "Когда привезти самокат"

    RENTAL_PERIOD_DD = By.XPATH, '//div[@class="Dropdown-control"]'  # Поле "Срок аренды"

    RENTAL_PERIOD_BUTTON_IN_DD = By.XPATH, '//*[text()="{}"]'  # Выпадающий список "Срок аренды"

    INPUT_FIELD_COLOR = By.XPATH, '//*[@id="{}"]'  # Поле "Выбор цвета"

    INPUT_FIELD_COMMENT = By.XPATH, '//*[@placeholder="Комментарий для курьера"]'  # Поле "Комментарий"

    STATION_DROP_DOWN = By.XPATH, '//*[text()="{}"]'  # Drop down со списком станций

    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'  # Кнопка "Далее"

    ORDER_BUTTON = By.XPATH, '//button[contains(@class,"Button_Middle") and text()="Заказать"]'  # Кнопка "Заказать"

    CONFIRM_BUTTON = By.XPATH, '//button[text()="Да"]'  # Кнопка подтвердить заказ

    ORDER_STATUS_BUTTON = By.XPATH, '//button[text()="Посмотреть статус"]'  # Кнопка "Посмотреть статус заказа"

    TITLE = By.XPATH, '//*[text()="Про аренду"]'  # Заголовок "Про аренду"

    LOGO_SCOOTER = By.XPATH, '//*[contains(@class, "Header_LogoScooter")]'  # Логотип "Самокат"


class Flags:
    SUCCESSFUL_ORDER_FLAG = 'Посмотреть статус'  # Флаг успешного оформления заказа (Кнопка "Посмотреть статус заказа"
