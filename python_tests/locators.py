class Urls:
    MAIN_PAGE = 'https://www.chitai-gorod.ru/'
    CART = 'cart'

class Modals:
    CHOOSE_CITY_BY_XPATH = "//*[contains(text(), 'Да, я здесь')]"
    NO_SUBSCRIPTION_BY_XPATH = "//*[contains(text(), 'Нет, спасибо')]"


class Carusel:
    ITEM_IN_SLIDER_BY_CLASS = "slider__item"
    ITEMM_TITLE_BY_XPATH = "//*[contains(@class,'product-title__head')]"
    BUY_BUTTON_BY_XPATH = "//*[contains(@class,'button action-button blue')]"

class Cart:
    PRODUCT_QUANTITY_BY_CLASS = 'app-title__append'
    MINI_CART_BADGE_BY_XPATH = "//*[contains(@class,'header-cart__badge')]"
    ADD_ITEM = "//*[contains(@class,'product-quantity__button product-quantity__button--right')]"
    DELETE_BOOK_BY_CLASS = 'cart-item__actions-icon'
    BOOK_REMOVED_BY_CLASS = 'item-removed__description-title'


